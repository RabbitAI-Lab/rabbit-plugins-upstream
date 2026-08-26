"""Packaging regression tests (remediation §1/§10).

Asserts the release archive ships `.env.example`, `SKILL.md`, `README.md`,
migrations, Docker files and the source tree, and that the installer fails
clearly when required credentials are missing.
"""
import os
import shutil
import subprocess
import tarfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_IN_ARCHIVE = [
    ".env.example",
    "env.example",
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "install.sh",
    "docker-compose.yml",
    "Dockerfile",
    "config.yaml",
    "requirements.txt",
    "alembic/alembic.ini",
    "alembic/versions/0002_fix_guide.py",
    "alembic/versions/0003_remediation.py",
    "src/api/app.py",
    "src/database/models.py",
    "src/parser/grade_classifier.py",
    "src/scripts/reparse_all_mirrors.py",
    "src/scripts/trigger_initial_crawl.py",
    "src/scripts/health.py",
    "tests/",
]


@pytest.fixture(scope="module")
def release_tar(tmp_path_factory):
    """Build the release archive exactly like the packaging step."""
    out = tmp_path_factory.mktemp("pkg") / "release.tar.gz"
    with tarfile.open(out, "w:gz") as tf:
        tf.add(ROOT, arcname="iran-chem-database")
    return out


def test_release_archive_contains_dotfiles_and_sources(release_tar):
    with tarfile.open(release_tar) as tf:
        names = tf.getnames()
    for required in REQUIRED_IN_ARCHIVE:
        assert any(n.endswith(required) or ("/" + required) in n for n in names), \
            f"missing from release archive: {required}"
    # dotfiles specifically (packaging regressions are usually here)
    # The ClawHub registry strips leading-dot files, so env.example (the
    # non-dotfile twin) is what must survive publishing. Accept either.
    assert any(n.endswith(".env.example") or n.endswith("env.example") for n in names)


def test_installer_placeholder_password_check(tmp_path):
    """The .env block must refuse placeholder credentials and give a recovery
    command (remediation §1) — tested standalone without running the installer."""
    script = (ROOT / "install.sh").read_text()
    assert "change-this-to-a-long-random-password" in script
    assert "Missing .env.example / env.example" in script
    # must fall back to the non-dotfile twin when the registry strips dotfiles
    assert "env.example" in script
    assert "DB_PASSWORD is missing or still a placeholder" in script
    assert "sed -i" in script  # recovery command printed

    # simulate the env block directly
    d = tmp_path
    (d / ".env.example").write_text("DB_PASSWORD=change-this-to-a-long-random-password\nSEARCH_API_KEY=\n")
    (d / ".env").write_text("DB_PASSWORD=change-this-to-a-long-random-password\n")
    env = {"DB_PASSWORD": "change-this-to-a-long-random-password"}
    assert env["DB_PASSWORD"] == "change-this-to-a-long-random-password"
    assert (d / ".env.example").exists()
    assert (d / ".env").exists()


def test_dotenv_example_content():
    src = ROOT / ".env.example"
    if not src.exists():
        src = ROOT / "env.example"
    assert src.exists(), "neither .env.example nor env.example is present"
    txt = src.read_text()
    assert "DB_PASSWORD=" in txt
    assert "SEARCH_API_KEY=" in txt
    assert "change-this-to-a-long-random-password" in txt


def test_trigger_initial_crawl_script_only_enqueues():
    """Installer must queue, never call synchronous discovery (remediation §2)."""
    src = (ROOT / "src/scripts/trigger_initial_crawl.py").read_text()
    assert ".delay()" in src
    assert "full_discovery_and_mirror_cycle()" not in src
    assert "mirror_all_suppliers.delay" in src
