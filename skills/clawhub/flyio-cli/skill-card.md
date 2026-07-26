## Description: <br>
Use the Fly.io flyctl CLI to deploy, diagnose, and operate Fly.io apps with read-only diagnostics by default and explicit approval before state-changing operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[justinburdett](https://clawhub.ai/user/justinburdett) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to inspect Fly.io app status, logs, configuration, releases, deployment failures, GitHub Actions deployment setup, and Fly Postgres workflows. It is intended to keep routine diagnostics read-only while requiring explicit approval for deploys, SSH commands, secret changes, scaling, machine, volume, database, or app-destroy operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing Fly.io operations can alter deployed apps, machines, secrets, scaling, volumes, databases, or destroy resources. <br>
Mitigation: Confirm the target app, account, operation, expected impact, and user approval before running deploys, SSH commands, secret changes, scaling, machine, volume, database, or app-destroy commands. <br>
Risk: Fly.io credentials can grant access to production cloud resources. <br>
Mitigation: Keep FLY_API_TOKEN protected and least-privileged where possible. <br>


## Reference(s): <br>
- [Safety policy](references/safety.md) <br>
- [Rails + Docker builds on Fly](references/rails-docker-builds.md) <br>
- [Fly + GitHub Actions](references/github-actions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to read-only diagnostics and asks for explicit approval before state-changing Fly.io operations.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
