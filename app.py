from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# JSON file path
DASHBOARDS_FILE = 'dashboards.json'

def load_dashboards():
    """Load dashboards from JSON file"""
    if os.path.exists(DASHBOARDS_FILE):
        with open(DASHBOARDS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"dashboards": []}

def save_dashboards(data):
    """Save dashboards to JSON file"""
    with open(DASHBOARDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/')
def home():
    """Home page with list of all dashboards"""
    data = load_dashboards()
    dashboards = data.get('dashboards', [])
    return render_template('index.html', dashboards=dashboards)

@app.route('/dashboard/<slug>')
def dashboard_detail(slug):
    """Dashboard detail page with embed"""
    data = load_dashboards()
    dashboards = data.get('dashboards', [])
    dashboard = next((d for d in dashboards if d.get('slug') == slug), None)
    
    if not dashboard:
        flash('Dashboard not found', 'error')
        return redirect(url_for('home'))
    
    return render_template('dashboard_detail.html', dashboard=dashboard)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/admin/add', methods=['GET', 'POST'])
def admin_add():
    """Admin page to add new dashboards"""
    if request.method == 'POST':
        data = load_dashboards()
        
        # Get form data
        dashboard = {
            'id': len(data.get('dashboards', [])) + 1,
            'name': request.form.get('name'),
            'slug': request.form.get('slug'),
            'description': request.form.get('description'),
            'embed_url': request.form.get('embed_url'),
            'dataset_url': request.form.get('dataset_url'),
            'pbix_url': request.form.get('pbix_url'),
            'tags': [tag.strip() for tag in request.form.get('tags', '').split(',') if tag.strip()],
            'created_at': datetime.now().isoformat()
        }
        
        # Validate required fields
        if not all([dashboard['name'], dashboard['slug'], dashboard['embed_url']]):
            flash('Please fill in all required fields (name, slug, embed_url)', 'error')
            return render_template('admin_add.html')
        
        # Add dashboard
        data['dashboards'].append(dashboard)
        save_dashboards(data)
        
        flash('Dashboard added successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('admin_add.html')

@app.after_request
def add_security_headers(response):
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    # Allow Power BI iframes and Tailwind CSS CDN
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*.powerbi.com https://*.powerbigov.us https://cdn.tailwindcss.com; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdn.tailwindcss.com; frame-src 'self' https://*.powerbi.com https://*.powerbigov.us; img-src 'self' data: https:; connect-src 'self' https://*.powerbi.com https://*.powerbigov.us; font-src 'self' data: https://cdn.jsdelivr.net https://cdn.tailwindcss.com;"
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
