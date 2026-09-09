const navToggle = document.querySelector('.nav-toggle');
const primaryNav = document.querySelector('#primary-nav');

const setTheme = (theme) => {
	const isDark = theme === 'dark';
	document.documentElement.dataset.theme = theme;
	document.querySelectorAll('[data-theme-toggle]').forEach((toggle) => {
		toggle.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
		toggle.querySelector('.theme-toggle-label').textContent = isDark ? 'Light mode' : 'Dark mode';
	});
	document.querySelector('meta[name="theme-color"]')?.setAttribute('content', isDark ? '#17181c' : '#f5f5f2');
};

const savedTheme = window.localStorage.getItem('dropnote-theme');
setTheme(savedTheme === 'dark' ? 'dark' : 'light');

document.querySelectorAll('[data-theme-toggle]').forEach((toggle) => {
	toggle.addEventListener('click', () => {
		const nextTheme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
		window.localStorage.setItem('dropnote-theme', nextTheme);
		setTheme(nextTheme);
	});
});

navToggle?.addEventListener('click', () => {
	const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
	navToggle.setAttribute('aria-expanded', String(!isOpen));
	primaryNav?.classList.toggle('is-open', !isOpen);
});

document.querySelector('[data-clear-search]')?.addEventListener('click', (event) => {
	const input = event.currentTarget.closest('form')?.querySelector('input[type="search"]');
	if (input) {
		input.value = '';
		input.focus();
	}
});

document.addEventListener('keydown', (event) => {
	if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') {
		event.preventDefault();
		document.querySelector('.dashboard-search input[type="search"]')?.focus();
	}
});

document.querySelectorAll('[data-note-form]').forEach((form) => {
	const content = form.querySelector('textarea[name="content"]');
	const counter = form.querySelector('[data-content-count]');
	if (!content || !counter) return;
	const updateCount = () => {
		const count = content.value.length;
		counter.textContent = `${count.toLocaleString()} character${count === 1 ? '' : 's'}`;
	};
	content.addEventListener('input', updateCount);
	updateCount();
});

document.querySelectorAll('[data-dismiss]').forEach((button) => {
	button.addEventListener('click', () => button.closest('.message')?.remove());
});

window.setTimeout(() => document.querySelectorAll('.message').forEach((message) => message.remove()), 5000);
