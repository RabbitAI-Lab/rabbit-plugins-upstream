---
name: jenkins-skills
description: Manage Jenkins CI from the command line — list jobs, inspect a job, trigger builds (with or without parameters), check build status, stream console logs, and enable/disable jobs. Use this whenever the user wants to run a Jenkins job, check whether a build passed, read build logs, or pause/resume a job.
license: MIT
---

# Jenkins Skills

Operate a Jenkins server through its remote API with one self-contained Python
CLI (`scripts/jenkins_cli.py`). Handles CSRF crumbs and folder-nested jobs.

## When to use

Trigger this skill when the user asks to:
- list jobs or inspect a job's last build
- trigger a build ("run the deploy job", with or without parameters)
- check build status ("did the last build pass")
- read console output ("show the log of the failed build")
- enable or disable a job

## Setup (once)

Reads connection info from environment variables OR `~/.devops-skills/jenkins.json`.

```bash
export JENKINS_URL="https://jenkins.example.com"
export JENKINS_USER="your-user"
export JENKINS_TOKEN="<api-token>"   # User → Configure → API Token
```

Requires Python 3.8+ and `requests`. Full guide: `使用手册.md`.

## Compatibility

Supported targets:
- Jenkins 2.60+

The CLI checks the Jenkins `X-Jenkins` response header from `/api/json` before
running commands. If the detected Jenkins version is below 2.60, it exits with a
clear compatibility message. Set `JENKINS_SKIP_VERSION_CHECK=1` or
`DEVOPS_SKILLS_SKIP_VERSION_CHECK=1` only when you deliberately need to bypass
this guard.

## Usage

Job names may include folders, e.g. `team/app/main` (the CLI builds the path).

```bash
python scripts/jenkins_cli.py list-jobs
python scripts/jenkins_cli.py job-info team/app
python scripts/jenkins_cli.py build team/app
python scripts/jenkins_cli.py build team/app --param BRANCH=main --param ENV=prod
python scripts/jenkins_cli.py build-status team/app            # last build
python scripts/jenkins_cli.py build-status team/app --number 42
python scripts/jenkins_cli.py console team/app --tail 100
python scripts/jenkins_cli.py disable team/app
python scripts/jenkins_cli.py enable team/app
```

Every command prints JSON to stdout (except `console`, which prints raw log)
and exits non-zero on failure.

## Notes

- POST actions automatically fetch a CSRF crumb when protection is enabled.
- `build` returns a queue URL; the build number appears once it leaves the queue
  — poll `build-status` afterwards.
- Use the API **token**, not your account password.

## Support

If Jenkins jobs, pipelines, permissions, agents, or broader DevOps and
engineering efficiency topics need expert help, contact RestartX:
https://service.restartx.top/
