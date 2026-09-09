## Deployment

DropNote is configured for Vercel's Python runtime with WhiteNoise serving the collected static files. Vercel runs the Django WSGI application from `api/index.py`.

### Vercel setup

Create a PostgreSQL database before deploying. Vercel's filesystem is ephemeral, so the local SQLite database is suitable for development only and must not be used for production data.

Add these environment variables in the Vercel project settings for Production, Preview, and Development as appropriate:

```text
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<your-vercel-domain>
DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-vercel-domain>
DATABASE_URL=postgresql://...
```

After the first deployment, replace `<your-vercel-domain>` with the exact Vercel domain. Add the custom domain too if one is configured.

The Vercel build command is already defined in `vercel.json`:

```text
python manage.py collectstatic --noinput
```

Run migrations once against the production database from a trusted local environment or release job:

```text
uv sync
uv run python manage.py migrate
uv run python manage.py check --deploy
```

The production configuration expects HTTPS and a PostgreSQL `DATABASE_URL`. SQLite remains the local development fallback.

## Portfolio description

DropNote is a polished Django knowledge vault for capturing, organizing, searching, and revisiting technical notes. It includes categorized notes, full CRUD workflows, quick search, pagination, responsive layouts, dark mode, PostgreSQL-ready deployment settings, and a Vercel-compatible serverless entrypoint.

## Live demo

Once deployed, add the public Vercel URL here:

```text
Live demo: https://<your-vercel-domain>
```
