from app.core.config import Settings


def test_default_database_url_uses_async_driver():
    assert Settings().database_url.startswith("postgresql+asyncpg://")


def test_environment_variable_overrides_default(monkeypatch):
    monkeypatch.setenv("GROQ_MODEL", "some-other-model")
    assert Settings().groq_model == "some-other-model"
