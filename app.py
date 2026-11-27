import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from cicd_service import CICDGuide

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="cicd-demo-secret-key-for-university-course",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["*"],
        MIDDLEWARE=[
            "django.middleware.common.CommonMiddleware",
        ],
    )
    django.setup()


def index(request):
    guide = CICDGuide(version="1.0")
    ctx = guide.get_page_context()

    cards_html = ""
    for stage in ctx["stages"]:
        cards_html += f"""
        <div class="card">
            <span class="badge">{stage['code']}</span>
            <h2>{stage['name']}</h2>
            <p>{stage['description']}</p>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>CI/CD — {ctx['course_title']}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{ max-width: 860px; margin: 0 auto; }}
        header {{
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            padding: 32px;
            border-radius: 16px;
            margin-bottom: 28px;
        }}
        .course {{ font-size: 14px; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; }}
        h1 {{ margin: 10px 0; font-size: 32px; }}
        .meta {{ font-size: 14px; background: rgba(0,0,0,0.25); display: inline-block;
                padding: 6px 12px; border-radius: 8px; margin-top: 8px; }}
        .card {{
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 16px;
        }}
        .badge {{
            background: #38bdf8;
            color: #0f172a;
            font-weight: bold;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 13px;
        }}
        h2 {{ margin: 12px 0 8px; font-size: 20px; color: #e2e8f0; }}
        p {{ margin: 0; color: #94a3b8; line-height: 1.6; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="course">Курс: «{ctx['course_title']}»</div>
            <h1>Теперь вы знаете как работает CI/CD и конвейер поставки</h1>
            <p style="color: #e2e8f0;">
                Автоматизированный процесс сборки, тестирования и доставки кода в продакшен.
            </p>
            <div class="meta">Версия релиза: <b>v{ctx['version']}</b> | Этапов: {ctx['total_stages']}</div>
        </header>
        {cards_html}
    </div>
</body>
</html>"""
    return HttpResponse(html)


urlpatterns = [
    path("", index, name="index"),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
