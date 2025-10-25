# Deployment Guide - Power BI Dashboard Viewer

This guide provides step-by-step instructions for deploying the Power BI Dashboard Viewer to Render and Railway.

## Prerequisites

Before deploying, ensure you have:
- A GitHub account
- Your project pushed to a GitHub repository
- A Power BI account with reports to embed

## Option 1: Deploy to Render

### Step 1: Push to GitHub

1. Create a new repository on GitHub (e.g., `powerbi-dashboard-viewer`)
2. Initialize git in your project directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/powerbi-dashboard-viewer.git
   git push -u origin main
   ```

### Step 2: Create Render Account

1. Go to https://render.com
2. Sign up for a free account (or sign in if you have one)
3. You'll get 750 hours/month free

### Step 3: Create Web Service

1. Click the "New +" button in the top right
2. Select "Web Service"
3. Connect your GitHub account (if not already connected)
4. Select your repository (`powerbi-dashboard-viewer`)
5. Click "Connect"

### Step 4: Configure the Service

Fill in the following details:

- **Name:** powerbi-dashboard-viewer (or your preferred name)
- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Instance Type:** Free (or choose a paid tier)

### Step 5: Add Environment Variables

Click "Advanced" and add:

- **Key:** `SECRET_KEY`
- **Value:** Generate a random string (you can use: `python -c "import secrets; print(secrets.token_hex(32))"`)

### Step 6: Deploy

1. Click "Create Web Service"
2. Wait for deployment (usually 2-5 minutes)
3. Your app will be available at: `https://your-app-name.onrender.com`

### Step 7: Verify

1. Open your public URL in a browser
2. You should see the home page with sample dashboards
3. Test the admin interface at `/admin/add`

## Option 2: Deploy to Railway

### Step 1: Push to GitHub

Same as Step 1 in Render deployment.

### Step 2: Create Railway Account

1. Go to https://railway.app
2. Sign up with GitHub
3. Railway provides $5/month free credit

### Step 3: Create New Project

1. Click "New Project" on the dashboard
2. Select "Deploy from GitHub repo"
3. Select your repository
4. Click "Deploy Now"

### Step 4: Configure Deployment

Railway auto-detects Python projects. Configure:

1. In your project, go to Settings → Environment
2. Add environment variable:
   - **Name:** `SECRET_KEY`
   - **Value:** Generate a random string

3. Go to Settings → Deployment
4. Set Start Command:
   ```
   gunicorn app:app
   ```

### Step 5: Get Public URL

1. Railway auto-generates a domain
2. Go to Settings → Domains
3. Your URL will be: `https://your-app.up.railway.app`

### Step 6: Verify

1. Open your public URL
2. Test all pages and functionality

## Post-Deployment Steps

### 1. Update Power BI URLs

1. Log into your deployed site
2. Go to `/admin/add`
3. Add your real Power BI dashboards with actual embed URLs
4. Or edit `dashboards.json` and redeploy

### 2. Configure Custom Domain (Optional)

**Render:**
- Go to your service → Settings → Custom Domains
- Add your domain
- Update DNS records

**Railway:**
- Go to Settings → Domains → Custom Domain
- Add your domain
- Update DNS records

### 3. Set Up Continuous Deployment

Both Render and Railway automatically redeploy when you push to GitHub.

1. Make changes locally
2. Commit and push to GitHub
3. Render/Railway automatically redeploys

## Generating SECRET_KEY

On your local machine:

```bash
# Windows PowerShell
python -c "import secrets; print(secrets.token_hex(32))"

# Linux/macOS
python3 -c "import secrets; print(secrets.token_hex(32))"
```

## Troubleshooting

### App Won't Start

**Problem:** `ModuleNotFoundError`

**Solution:** Ensure `requirements.txt` includes all dependencies

---

**Problem:** `Port already in use`

**Solution:** Railway/Render manage ports automatically. Check start command is `gunicorn app:app`

---

### Power BI Reports Not Loading

**Problem:** Blank iframe or error message

**Solution:**
1. Verify embed URL is correct
2. Check CSP settings in `app.py`
3. Ensure Power BI report is public (for "Publish to web")
4. Check browser console for errors

---

### Build Fails

**Problem:** Build command fails

**Solution:**
1. Check `Procfile` exists
2. Verify `requirements.txt` is correct
3. Check Python version in `runtime.txt`

---

### Environment Variables Not Working

**Problem:** SECRET_KEY not being read

**Solution:**
1. Verify variable name is exactly `SECRET_KEY`
2. Check it's set in the platform's environment settings
3. Redeploy after adding variables

## Monitoring

### Render
- View logs: Dashboard → Your Service → Logs
- Monitor metrics in the Metrics tab

### Railway
- View logs: Project → Deployments → View Logs
- Monitor in the Metrics tab

## Updating Your App

1. Make changes locally
2. Test locally with `flask run`
3. Commit changes:
   ```bash
   git add .
   git commit -m "Update dashboards"
   git push
   ```
4. Platform automatically deploys new version

## Rollback

### Render
- Go to Deploys tab
- Click on previous successful deploy
- Click "Rollback"

### Railway
- Go to Deployments
- Click on previous deployment
- Click "Redeploy"

## Cost Estimation

### Render (Free Tier)
- 750 hours/month free
- 0.5 GB RAM
- Perfect for small projects

### Railway
- $5/month credit
- Pay as you go after credit
- More resources available

## Security Considerations

1. **Change SECRET_KEY:** Always use a strong, unique SECRET_KEY
2. **Add Authentication:** Consider adding auth to admin routes in production
3. **CSP:** Review Content Security Policy for your specific use case
4. **HTTPS:** Both platforms provide HTTPS automatically

## Getting Help

- **Render Support:** https://render.com/docs
- **Railway Support:** https://docs.railway.app
- **Flask Docs:** https://flask.palletsprojects.com

## Next Steps

After deployment:
1. Test all functionality on your live site
2. Update sample dashboards with your Power BI URLs
3. Share your public URL with users
4. Monitor usage and logs
5. Consider adding custom domain
6. Set up monitoring/alerting (optional)
