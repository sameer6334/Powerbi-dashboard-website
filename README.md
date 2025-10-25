# Power BI Dashboard Viewer

A simple, responsive Flask website to list and open Power BI dashboards. The site is mobile-first, easy to maintain, and allows you to add new dashboards without changing code.

## Features

- 📊 **Browse Dashboards**: View all available Power BI dashboards in a clean, card-based layout
- 📱 **Mobile-First Design**: Fully responsive interface using Tailwind CSS
- 🔗 **Embedded Reports**: Interactive Power BI reports embedded in the browser
- 📥 **Download Resources**: Access datasets and Power BI project files (.pbix)
- ➕ **Easy Management**: Simple admin interface to add new dashboards
- 🔒 **Security Headers**: Configured CSP and security headers for production

## Local Development

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup

1. **Clone or download this repository**

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

5. **Run the application**:
```bash
flask run
```

6. **Open your browser** and navigate to `http://localhost:5000`

## Adding Dashboards

### Method 1: Using the Admin Interface

1. Navigate to `http://localhost:5000/admin/add` or click "Add Dashboard" in the navigation
2. Fill in the form with:
   - **Dashboard Name**: Display name for the dashboard
   - **URL Slug**: URL-friendly identifier (e.g., `sales-analytics`)
   - **Description**: Brief description of the dashboard
   - **Power BI Embed URL**: The embed URL from Power BI's "Publish to web" or embed option
   - **Dataset URL** (optional): Link to the dataset (CSV/Excel/Google Drive)
   - **PBIX File URL** (optional): Link to download the .pbix file
   - **Tags** (optional): Comma-separated tags (e.g., `sales, analytics, monthly`)
3. Click "Add Dashboard"

### Method 2: Edit dashboards.json Directly

1. Open `dashboards.json` in a text editor
2. Add a new dashboard object to the `dashboards` array:

```json
{
  "id": 3,
  "name": "Your Dashboard Name",
  "slug": "your-dashboard-slug",
  "description": "Dashboard description",
  "embed_url": "https://app.powerbi.com/view?r=YOUR_EMBED_URL",
  "dataset_url": "https://example.com/your-dataset.csv",
  "pbix_url": "https://example.com/your-file.pbix",
  "tags": ["tag1", "tag2"],
  "created_at": "2024-01-01T12:00:00"
}
```

3. Save the file and restart the Flask application

### Getting Power BI Embed URLs

1. **Publish to Web** (Public):
   - Open your Power BI report in Power BI Service
   - Click "File" → "Embed" → "Publish to web (public)"
   - Copy the generated iframe embed URL

2. **Standard Embed**:
   - Open your Power BI report in Power BI Service
   - Click "File" → "Embed" → "Website or portal"
   - Copy the embed URL

## Deployment

### Deploy to Render

1. **Push your code to GitHub**:
   - Create a new repository on GitHub
   - Push this project to the repository

2. **Connect to Render**:
   - Go to https://render.com
   - Sign up or log in
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure the deployment**:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment Variables**: Add `SECRET_KEY` (generate a random key)

4. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Your public URL will be shown (e.g., `https://your-app.onrender.com`)

### Deploy to Railway

1. **Push your code to GitHub**:
   - Create a new repository on GitHub
   - Push this project to the repository

2. **Connect to Railway**:
   - Go to https://railway.app
   - Sign up or log in
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

3. **Configure the deployment**:
   - Railway auto-detects Python projects
   - Add environment variable: `SECRET_KEY` (generate a random key)
   - Set start command to: `gunicorn app:app`

4. **Deploy**:
   - Railway automatically detects the project and deploys
   - Your public URL will be shown (e.g., `https://your-app.up.railway.app`)

### Getting Your Public URL

After deployment:
- **Render**: Check the "Dashboard" tab for your URL (e.g., `https://your-app.onrender.com`)
- **Railway**: Check the "Settings" tab for the "Generate Domain" or "Custom Domain" option

## Project Structure

```
.
├── app.py                  # Main Flask application
├── dashboards.json        # Dashboard data (JSON file)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # Home page
    ├── dashboard_detail.html  # Dashboard detail page
    ├── about.html        # About page
    └── admin_add.html    # Admin form to add dashboards
```

## Security Notes

- **Content Security Policy (CSP)**: Configured to allow Power BI iframes and scripts
- **Security Headers**: X-Content-Type-Options, X-Frame-Options, X-XSS-Protection
- **SECRET_KEY**: Change the default secret key in production
- **No Authentication**: The admin interface is currently public. Add authentication if needed

## Customization

### Adjust Content Security Policy

If you need to modify CSP settings for different embed methods:

1. Edit `app.py`
2. Find the `add_security_headers` function
3. Modify the `Content-Security-Policy` header

Example for Power BI Embedded (Azure):
```python
response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://embedded.powerbi.com; ..."
```

### Styling

The application uses Tailwind CSS via CDN. To customize:

1. Edit templates in the `templates/` directory
2. Modify Tailwind classes or add custom CSS in `templates/base.html`

## Troubleshooting

### Power BI Reports Not Displaying

- Check that the embed URL is correct
- Verify CSP settings allow Power BI domains
- Ensure the Power BI report is public or accessible
- Check browser console for CSP violations

### Deployment Issues

- Ensure `gunicorn` is in `requirements.txt`
- Check that the start command is set correctly
- Verify environment variables are configured
- Check deployment logs for errors

## License

MIT License - feel free to use this project for your own purposes.

## Support

For issues or questions, please open an issue on the repository.
