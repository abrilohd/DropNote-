# DropNote

DropNote is a focused knowledge vault for saving technical notes before useful ideas disappear. Create notes, organize them by category, search across your collection, and return to the details that matter.

## Portfolio Description

DropNote is a full-stack Django application for capturing, organizing, searching, and revisiting technical knowledge. It includes categorized note management, search, pagination, responsive templates, dark mode, Django admin support, PostgreSQL integration, and a Vercel-ready production deployment.

Built with Django, PostgreSQL, HTML, CSS, and JavaScript.

## Live Demo

The live demo URL will be added after the Vercel deployment succeeds:

```text
https://<your-project>.vercel.app
```

Do not open this placeholder URL. Replace it with the exact domain shown in Vercel under **Settings > Domains**.

## Deployment On Vercel

The repository is configured for Vercel's Python runtime. `api/index.py` loads the Django WSGI application, and `vercel.json` routes requests and collects static files.

Vercel's filesystem is ephemeral. Use an external PostgreSQL provider such as Neon or Supabase for production data. SQLite is only for local development.

### 1. Import the repository

1. Open Vercel and select **Add New Project**.
2. Import `abrilohd/DropNote-` from GitHub.
3. Keep the root directory as `./`.
4. Keep the detected Django preset.
5. Click **Deploy**.

If Vercel shows a deployment as **Canceled**, create a new deployment from the latest `main` commit instead of trying to use the canceled URL.

### 2. Create PostgreSQL

Create a PostgreSQL database with Neon, Supabase, or another PostgreSQL provider. Copy the complete connection string.

### 3. Add environment variables

In Vercel, open **Settings > Environment Variables** and add these values for Production. Add them to Preview too if you want preview deployments to work.

```text
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<your-project>.vercel.app
DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-project>.vercel.app
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>
```

Use the exact domain from **Settings > Domains**. For a custom domain, include both domains as comma-separated values:

```text
DJANGO_ALLOWED_HOSTS=<your-project>.vercel.app,www.example.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-project>.vercel.app,https://www.example.com
```

Never commit `DATABASE_URL` or `DJANGO_SECRET_KEY` to GitHub.

### 4. Run migrations

After creating the database, run migrations against the production database from a secure terminal. On PowerShell:

```powershell
$env:DATABASE_URL="your-production-postgresql-url"
uv run python manage.py migrate
```

If `uv` is unavailable, use the project virtual environment:

```powershell
$env:DATABASE_URL="your-production-postgresql-url"
.\.venv\Scripts\python.exe manage.py migrate
```

### 5. Redeploy and test

After adding variables and running migrations, open **Deployments**, select the latest `main` deployment, and choose **Redeploy**.

Test these URLs using the real Vercel domain:

```text
https://<your-project>.vercel.app/
https://<your-project>.vercel.app/notes/
https://<your-project>.vercel.app/notes/new/
https://<your-project>.vercel.app/admin/
```

Also test creating, editing, deleting, searching, and filtering notes. Confirm that CSS, JavaScript, and dark mode load correctly.

### Local validation

```powershell
uv sync
uv run python manage.py collectstatic --noinput
uv run python manage.py check --deploy
```
