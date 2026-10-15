## Description:

Helps operators diagnose and manage pipelines, runners, artifacts, and repository settings on self-managed GitLab and Gitea servers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD operators use this skill to investigate failed pipelines, runner queues, artifact storage, and stale repository work on self-managed GitLab or Gitea, and to perform approved corrective actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CI/CD write operations have no enforced local approval or read-only gate.

Mitigation: Use a least-privilege or read-only GitLab/Gitea token by default and require agent-side approval before writes.

Risk: Artifact deletion is irreversible, even when recorded in the audit log.

Mitigation: Review the dry-run scope, specify an appropriate age threshold, and explicitly approve deletion before proceeding.

Risk: The deprecated plaintext token environment variable can expose credentials.

Mitigation: Use the encrypted token store instead and avoid the legacy plaintext token variable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/cicd-aiops)
- [Project homepage](https://github.com/AIops-tools/CICD-AIops)
- [Capabilities reference](artifact/references/capabilities.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes diagnostic findings and suggested next steps; available actions depend on the server platform and token permissions.]

## Skill Version(s):

0.12.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
