from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime

app = FastAPI()

@app.get("/api", response_class=HTMLResponse)
async def read_items():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
        <head>
            <title>FastAPI Dashboard</title>
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f1f5f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                .container {{ background: white; padding: 2.5rem; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); width: 400px; }}
                .status-badge {{ background: #dcfce7; color: #166534; padding: 6px 12px; border-radius: 99px; font-size: 0.85rem; font-weight: 600; display: inline-block; margin-bottom: 1rem; }}
                h1 {{ color: #1e293b; margin: 0; font-size: 1.8rem; }}
                .info-item {{ display: flex; justify-content: space-between; margin-top: 1.5rem; padding-bottom: 0.8rem; border-bottom: 1px solid #f1f5f9; }}
                .label {{ color: #64748b; font-weight: 500; }}
                .value {{ color: #0f172a; font-weight: 600; }}
                .back-btn {{ margin-top: 2rem; display: block; text-align: center; color: #6366f1; text-decoration: none; font-weight: 600; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="status-badge"><i class="fas fa-check-circle"></i> System Online</div>
                <h1>FastAPI Live Service</h1>
                <div class="info-item">
                    <span class="label">Response Status</span>
                    <span class="value" style="color: #10b981;">Success</span>
                </div>
                <div class="info-item">
                    <span class="label">Server Time</span>
                    <span class="value">{current_time}</span>
                </div>
                <div class="info-item">
                    <span class="label">Route Path</span>
                    <span class="value">/api</span>
                </div>
                <a href="/" class="back-btn"><i class="fas fa-arrow-left"></i> 돌아가기</a>
            </div>
        </body>
    </html>
    """

@app.get("/")
async def root():
    return {"status": "healthy", "service": "fastapi-app"}