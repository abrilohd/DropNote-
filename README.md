## Deployment

DropNote is ready to deploy on Railway as a Django web service. Railway uses the Nixpacks builder, runs migrations before each deployment, and starts the app with Gunicorn using the configuration in `railway.json`.

### Railway setup

1. Create a new Railway project from the GitHub repository `abrilohd/DropNote-`.
2. Add a PostgreSQL service to the same project.
3. In the Django service variables, add the PostgreSQL service's `DATABASE_URL` reference and these values:

```text
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<railway-domain>,<custom-domain>
DJANGO_CSRF_TRUSTED_ORIGINS=https://<railway-domain>,https://<custom-domain>
```

4. Deploy the `main` branch.
5. Generate a Railway public domain in the service's Networking settings.
6. Replace `<railway-domain>` with that exact hostname, redeploy, and verify the live site.

The production database must be PostgreSQL. SQLite remains the local development fallback because Railway's filesystem is not intended for persistent application data.

The Railway service uses these commands automatically:

```text
Build: Nixpacks detects Python and installs requirements.txt
Pre-deploy: python manage.py migrate
Start: gunicorn config.wsgi:application
```

Before deploying, validate locally:

```text
uv sync
uv run python manage.py collectstatic --noinput
uv run python manage.py check --deploy
```

### Optional Vercel deployment

The repository also retains a Vercel-compatible serverless entrypoint in `api/index.py` and routing in `vercel.json`. Railway is the recommended deployment target because it provides a persistent PostgreSQL service and a conventional long-running Django process.

## Portfolio description

DropNote is a polished Django knowledge vault for capturing, organizing, searching, and revisiting technical notes. It includes categorized notes, full CRUD workflows, quick search, pagination, responsive layouts, dark mode, PostgreSQL-ready deployment settings, and a Railway-ready production service.

## Live demo

After the Railway deployment is live, add the public URL here:

```text
Live demo: https://<your-railway-domain>
```
