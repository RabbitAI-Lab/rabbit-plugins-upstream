"""Checks for the --diff-git plumbing and the gitops parameterization.

No LLM is invoked — these exercise the pure helpers plus a throwaway git repo.
"""
import json
import os
import subprocess

import pytest

import adversarial_review as review
from adversarial_common import gitops


def _git(workdir, *args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=workdir, check=True,
    ).stdout.strip()


def _write(workdir, name, content):
    path = os.path.join(workdir, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        fh.write(content)


@pytest.fixture
def repo(tmp_path):
    gitops.auto_init(str(tmp_path))
    return str(tmp_path)


# --- gitops parameterization (spec: create_loop_branch / get_diff) ---------

def test_create_loop_branch_default_prefix_unchanged(repo):
    assert gitops.create_loop_branch(repo, "feat", "main") == "loop/feat/1"


def test_create_loop_branch_custom_prefix(repo):
    name = gitops.create_loop_branch(repo, "cool thing", "main", prefix="review")
    assert name == "review/cool-thing/1"
    assert gitops.branch_exists(repo, name)


def test_get_diff_passes_extra_args(repo):
    _write(repo, "d.txt", "one\n")
    gitops.commit_all(repo, "base")
    base_sha = gitops.head_sha(repo)
    _write(repo, "d.txt", "one\ntwo\n")
    gitops.commit_all(repo, "edit")
    stat = gitops.get_diff(repo, base_sha, "HEAD", "--stat")
    assert "d.txt" in stat and "1 insertion" in stat
    # default (no extra args) is still the raw diff
    raw = gitops.get_diff(repo, base_sha, "HEAD")
    assert "+two" in raw and "insertion" not in raw


# --- resolve_base precedence (--base > $ACR_BASE > main > master) ---------

def test_resolve_base_defaults_to_main(repo):
    assert review.resolve_base(repo, None) == "main"


def test_resolve_base_flag_beats_env(repo, monkeypatch):
    _git(repo, "branch", "develop", "main")
    monkeypatch.setenv("ACR_BASE", "develop")
    assert review.resolve_base(repo, "main") == "main"


def test_resolve_base_env_when_no_flag(repo, monkeypatch):
    _git(repo, "branch", "develop", "main")
    monkeypatch.setenv("ACR_BASE", "develop")
    assert review.resolve_base(repo, None) == "develop"


def test_resolve_base_master_fallback(repo):
    # Rename main -> master so only master exists.
    _git(repo, "branch", "-m", "main", "master")
    assert review.resolve_base(repo, None) == "master"


def test_resolve_base_bad_flag_falls_through_to_main(repo):
    # The spec's "--base > $ACR_BASE > main > master" is an ordered fallback
    # chain: a --base that does not resolve keeps trying the rest.
    assert review.resolve_base(repo, "definitely-not-a-branch") == "main"


def test_resolve_base_raises_when_nothing_exists(repo):
    _git(repo, "branch", "-m", "main", "trunk")  # neither main nor master now
    with pytest.raises(review.ReviewError):
        review.resolve_base(repo, None)


# --- worktree path + diff parsing ------------------------------------------

def test_next_worktree_path_increments(tmp_path):
    assert review.next_worktree_path("feat", root=str(tmp_path)) == tmp_path / "review-feat-1"
    (tmp_path / "review-feat-1").mkdir()
    assert review.next_worktree_path("feat", root=str(tmp_path)) == tmp_path / "review-feat-2"


def test_changed_files_from_diff():
    diff = (
        "diff --git a/a.py b/a.py\n"
        "--- a/a.py\n"
        "+++ b/a.py\n"
        "@@ -1 +1 @@\n"
        "-old\n"
        "+new\n"
        "diff --git a/b.py b/b.py\n"
        "--- /dev/null\n"
        "+++ b/b.py\n"
    )
    assert review.changed_files_from_diff(diff) == ["a.py", "b.py"]


def test_build_project_source_prepends_diff(repo):
    diff = "diff --git a/x.py b/x.py\n+++ b/x.py\n@@ -0,0 +1 @@\n+hi\n"
    _write(repo, "x.py", "hi\n")
    branch_point = "0123456789abcdef"
    src = review.build_project_source(repo, diff, branch_point=branch_point)
    assert src["code_text"].index("DIFF") < src["code_text"].index("File contents")
    assert "--- x.py ---" in src["code_text"]
    assert src["project_dir"] == repo
    assert branch_point in src["code_text"]
    assert f"git diff {branch_point}..HEAD" in src["code_text"]
    assert "HEAD~1" not in src["code_text"]


def test_build_project_source_treats_whitespace_diff_as_input(repo):
    _write(repo, "x.py", "value = 1\n")

    src = review.build_project_source(repo, " \n")

    assert src["context_kind"] == "input"
    assert src["context_text"] == "--- x.py ---\nvalue = 1\n"
    assert "=== DIFF" not in src["code_text"]


def test_build_project_source_rejects_parent_path_escape(tmp_path):
    project = tmp_path / "workspace" / "project"
    project.mkdir(parents=True)
    sentinel = "PARENT_PATH_SENTINEL"
    (tmp_path / "secret.txt").write_text(sentinel)
    diff = (
        "diff --git a/../../secret.txt b/../../secret.txt\n"
        "+++ b/../../secret.txt\n"
        "@@ -0,0 +1 @@\n"
        "+malicious\n"
    )

    src = review.build_project_source(project, diff)

    assert sentinel not in src["code_text"]


def test_build_project_source_rejects_symlink_escape(tmp_path):
    project = tmp_path / "project"
    project.mkdir()
    sentinel = "SYMLINK_ESCAPE_SENTINEL"
    secret = tmp_path / "secret.txt"
    secret.write_text(sentinel)
    (project / "linked.txt").symlink_to(secret)
    diff = (
        "diff --git a/linked.txt b/linked.txt\n"
        "+++ b/linked.txt\n"
        "@@ -0,0 +1 @@\n"
        "+malicious\n"
    )

    src = review.build_project_source(project, diff)

    assert sentinel not in src["code_text"]


def test_build_project_source_allows_valid_nested_file(tmp_path):
    project = tmp_path / "project"
    nested = project / "src" / "package"
    nested.mkdir(parents=True)
    content = "VALID_NESTED_CONTENT\n"
    (nested / "module.py").write_text(content)
    diff = (
        "diff --git a/src/package/module.py b/src/package/module.py\n"
        "+++ b/src/package/module.py\n"
        "@@ -0,0 +1 @@\n"
        "+VALID_NESTED_CONTENT\n"
    )

    src = review.build_project_source(project, diff)

    assert "--- src/package/module.py ---\n" + content in src["code_text"]


# --- build_dir_source containment parity (spec: CR2 blocker) -------------

def test_build_dir_source_rejects_parent_path_escape(tmp_path, monkeypatch):
    project = tmp_path / "workspace" / "project"
    project.mkdir(parents=True)
    sentinel = "PARENT_PATH_SENTINEL"
    (tmp_path / "secret.txt").write_text(sentinel)
    # _list_tree never yields ".." for real on-disk files; inject the escape
    # directly to exercise build_dir_source's containment guard (R1).
    monkeypatch.setattr(review, "_list_tree", lambda root: ["../../secret.txt"])

    src = review.build_dir_source(project)

    assert sentinel not in src["code_text"]


def test_build_dir_source_rejects_symlink_escape(tmp_path):
    project = tmp_path / "project"
    project.mkdir()
    sentinel = "SYMLINK_ESCAPE_SENTINEL"
    secret = tmp_path / "secret.txt"
    secret.write_text(sentinel)
    (project / "linked.txt").symlink_to(secret)

    src = review.build_dir_source(project)

    assert sentinel not in src["code_text"]


def test_build_dir_source_warns_on_skipped_symlink(tmp_path, capsys):
    project = tmp_path / "project"
    project.mkdir()
    sentinel = "SYMLINK_ESCAPE_SENTINEL"
    secret = tmp_path / "secret.txt"
    secret.write_text(sentinel)
    (project / "linked.txt").symlink_to(secret)

    review.build_dir_source(project)

    err = capsys.readouterr().err
    assert "linked.txt" in err
    assert "resolves outside" in err


def test_build_project_source_warns_on_skipped_symlink(tmp_path, capsys):
    project = tmp_path / "project"
    project.mkdir()
    sentinel = "SYMLINK_ESCAPE_SENTINEL"
    secret = tmp_path / "secret.txt"
    secret.write_text(sentinel)
    (project / "linked.txt").symlink_to(secret)
    diff = (
        "diff --git a/linked.txt b/linked.txt\n"
        "+++ b/linked.txt\n"
        "@@ -0,0 +1 @@\n"
        "+malicious\n"
    )

    review.build_project_source(project, diff)

    err = capsys.readouterr().err
    assert "linked.txt" in err
    assert "resolves outside" in err


def test_build_dir_source_warns_on_resolution_error(tmp_path, capsys):
    project = tmp_path / "project"
    project.mkdir()
    looped = project / "looped.txt"
    looped.symlink_to(looped)  # self-referential symlink: resolve() raises

    review.build_dir_source(project)

    err = capsys.readouterr().err
    assert "looped.txt" in err
    assert "WARNING: skipping" in err


def test_build_project_source_warns_on_resolution_error(tmp_path, capsys):
    project = tmp_path / "project"
    project.mkdir()
    looped = project / "looped.txt"
    looped.symlink_to(looped)  # self-referential symlink: resolve() raises
    diff = (
        "diff --git a/looped.txt b/looped.txt\n"
        "+++ b/looped.txt\n"
        "@@ -0,0 +1 @@\n"
        "+malicious\n"
    )

    review.build_project_source(project, diff)

    err = capsys.readouterr().err
    assert "looped.txt" in err
    assert "WARNING: skipping" in err


# --- CLI wiring -----------------------------------------------------------

def test_cli_diff_git_in_source_group():
    args = review.parse_args(["--diff-git", "--base", "develop"])
    assert args.diff_git is True
    assert args.base == "develop"
    assert args.allow_fallback is False


def test_cli_source_group_is_mutually_exclusive():
    with pytest.raises(SystemExit):
        review.parse_args(["--diff-git", "--diff", "x.patch"])


def test_r1_run_diff_git_context_gating_before_worktree(repo, tmp_path, monkeypatch):
    """R1: context gating runs before git worktree add; a too-short diff blocks.

    A one-line diff with min_source_lines=10 should trigger _preflight_source
    to block, and _worktree_add must never be called. Blocked exit writes final.json.
    """
    # Create a feature branch with one small change so we get a real diff against main
    _git(repo, "checkout", "-b", "feature/small")
    _write(repo, "small.py", "one line of change\n")
    gitops.commit_all(repo, "add small change")

    calls = []
    original_worktree_add = review._worktree_add

    def tracking_worktree_add(workdir, path, commit):
        calls.append(("worktree_add", path, commit))
        return original_worktree_add(workdir, path, commit)

    monkeypatch.setattr(review, "_worktree_add", tracking_worktree_add)
    monkeypatch.setattr(os, "getcwd", lambda: repo)

    out = tmp_path / "blocked_out"

    import argparse
    args = argparse.Namespace()
    args.base = "main"
    args.feature = None
    args.allow_fallback = False
    args.out = str(out)
    args.max_retries = 3
    args.max_input_chars = review.runner.DEFAULT_MAX_INPUT_CHARS
    args.max_output_chars = review.runner.DEFAULT_MAX_OUTPUT_CHARS
    args.truncate_input = False
    args.show_costs = False
    args.concurrency = None
    args.max_concurrency = 6
    args.max_agents = 6
    args.min_chars = None
    args.min_tokens = None
    args.min_source_lines = None

    # Require at least 10 source lines — we only have 1
    monkeypatch.setenv("ACR_MIN_SOURCE_LINES", "10")

    code = review.run_diff_git(args)

    assert code == review.EXIT_CONTEXT_BLOCKED
    assert calls == []  # worktree_add never called

    final = json.loads((out / "final.json").read_text())
    assert final["verdict"] == "CONTEXT_BLOCKED"
    assert final["status"] == "blocked"
    assert final["reason"] == "below_min_source_lines"
    assert "thresholds" in final
    assert final["thresholds"]["min_source_lines"] == 10


def test_git_failure_returns_infra_and_writes_final_json(tmp_path, monkeypatch):
    def fail_git(_args):
        raise gitops.GitError("mock git failure")

    monkeypatch.setattr(review, "run_diff_git", fail_git)

    code = review.main(["--diff-git", "--out", str(tmp_path)])

    assert code == review.EXIT_INFRA
    final = json.loads((tmp_path / "final.json").read_text())
    assert final["verdict"] == "ERROR"
    assert "mock git failure" in final["error"]
