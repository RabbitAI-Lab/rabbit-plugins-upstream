## Description:

Deploy or update Puter-hosted web apps/sites with a CLI-first, verify-first workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[logclinker](https://clawhub.ai/user/logclinker)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to deploy, update, verify, troubleshoot, and prepare rollback notes for Puter-hosted web apps and sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through deployment actions using the user's authenticated Puter CLI session.

Mitigation: Install and use it only when the agent is intended to build, deploy, and verify Puter-hosted web apps with that session.

Risk: Production targets or existing Puter apps/sites may be overwritten if a deployment target is wrong.

Mitigation: Require explicit confirmation before overwriting production targets and verify the target app, site identifier, and expected URL before deployment.

Risk: URL verification can be misused against untrusted or unintended URLs.

Mitigation: Run verification only against trusted public or Puter deployment URLs and require HTTP 200 plus the expected content marker when provided.

Risk: Fallback API behavior may be unclear for the installed Puter CLI or host version.

Mitigation: Review API fallback actions before execution, reuse authenticated context without exposing secrets, and inspect current CLI behavior before pushing through fallback paths.

## Reference(s):

- [Puter Deploy Checklist](references/deploy-checklist.md)
- [Puter API Fallback](references/api-fallback.md)
- [Puter Deploy Failure Playbook](references/failure-playbook.md)
- [ClawHub Skill Page](https://clawhub.ai/logclinker/skills/puter-deployer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and deployment report fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes verification status, deployment URL, source commit, rollback artifact, rollback command, and failure classification when applicable.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
