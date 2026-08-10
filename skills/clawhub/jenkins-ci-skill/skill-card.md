## Description:

Manage Jenkins CI from the command line: list jobs, inspect jobs, trigger builds, check build status, stream console logs, and enable or disable jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weiguang1017](https://clawhub.ai/user/weiguang1017)

### License/Terms of Use:

MIT

## Use Case:

Developers and DevOps engineers use this skill to inspect Jenkins jobs and builds, trigger regular or parameterized builds, review console output, and enable or disable jobs through the Jenkins Remote API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Build, enable, and disable actions can change Jenkins job state using configured Jenkins credentials.

Mitigation: Use a least-privilege Jenkins API token scoped to approved jobs and require human confirmation before build, enable, or disable actions.

Risk: Local Jenkins token configuration can expose credentials if stored insecurely.

Mitigation: Prefer environment variables or protect ~/.devops-skills/jenkins.json with restrictive permissions and keep it out of version control.

Risk: The security summary recommends updating the requests dependency floor before sensitive use.

Mitigation: Review and update the requests version constraint before deploying this skill in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weiguang1017/skills/jenkins-ci-skill)
- [Server-resolved source repository](https://github.com/weiguang1017/jenkins-ci-skill)
- [README](README.md)
- [Chinese usage manual](使用手册.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI commands return JSON except console logs, which return plain text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Jenkins connection settings from environment variables or ~/.devops-skills/jenkins.json.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
