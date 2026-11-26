from django.test import Client
from cicd_service import CICDGuide


def test_stages_count():
    guide = CICDGuide(version="1.0")
    assert guide.get_stages_count() == 3


def test_find_stage_by_code():
    guide = CICDGuide()
    ci_stage = guide.get_stage_by_code("ci")
    assert ci_stage is not None
    assert "Continuous Integration" in ci_stage["name"]
    assert guide.get_stage_by_code("UNKNOWN") is None


def test_page_context_structure():
    guide = CICDGuide(version="2.5")
    context = guide.get_page_context()
    assert context["version"] == "2.5"
    assert context["course_title"] == "Технологии внедрения программного обеспечения"
    assert len(context["stages"]) == 3


def test_django_index_page_renders():
    client = Client()
    response = client.get("/")
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assert "Что такое CI/CD" in content
    assert "Continuous Integration" in content
    assert "Технологии внедрения программного обеспечения" in content
