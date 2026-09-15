## Description:

cicd-aiops helps agents inspect and operate self-managed GitLab and self-hosted Gitea CI/CD environments, including projects, pipelines, runners, artifacts, repository hygiene, root-cause analyses, and governed write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DevOps engineers, and CI/CD operators use this skill to investigate GitLab or Gitea pipeline failures, runner capacity, artifact storage, stale work, and selected remediation actions on self-managed servers. It is intended for GitLab/Gitea CI/CD operations and is not a general infrastructure, Kubernetes deployment, or SaaS GitLab.com/Gitea Cloud skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact GitLab/Gitea write actions, including retrying or canceling pipelines, changing runner state, updating branch protection, and deleting artifacts.

Mitigation: Use read-only or narrowly scoped project tokens by default, require dry-run review for destructive actions, and grant write or admin-capable tokens only for the specific operations that need them.

Risk: Secret handling depends on the local configuration and can fall back to legacy plaintext token environment variables.

Mitigation: Use the encrypted secret store unlocked by CICD_AIOPS_MASTER_PASSWORD, avoid storing the master password directly in MCP config, and migrate away from legacy plaintext token environment variables.

Risk: Audit logs record activity after execution and are not approval controls.

Mitigation: Treat audit records as accountability evidence, pair them with external approval or operator review where needed, and pin the package to a reviewed version before enabling write tools.

Risk: The release is mock-validated and has no recorded end-to-end run against a live GitLab or Gitea server.

Mitigation: Validate the configured target with cicd-aiops doctor and test representative read and write workflows in a controlled environment before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/cicd-aiops)
- [Project homepage](https://github.com/AIops-tools/CICD-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool-call guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger CI/CD server API reads or writes through configured GitLab/Gitea credentials; write actions should be dry-run reviewed and constrained by token scope.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
