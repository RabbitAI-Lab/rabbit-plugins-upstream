## Description:

CICD AIops helps agents inspect and operate self-managed GitLab and self-hosted Gitea CI/CD servers, including pipelines, jobs, runners, artifacts, branch protection, releases, root-cause analyses, and governed write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DevOps engineers, and CI/CD operators use this skill to query self-managed GitLab or self-hosted Gitea environments, investigate failing pipelines, runner capacity, artifact storage, and stale repository work, and perform controlled maintenance actions when their token permits it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write-capable GitLab or Gitea operations when connected with a token that has write or admin scopes.

Mitigation: Use a dedicated least-privilege token by default, keep observe-only sessions on read-only credentials, and enable write or admin scopes only for deliberate maintenance sessions.

Risk: The master password and local audit database may expose sensitive CI/CD access or operational history if handled carelessly.

Mitigation: Avoid storing the master password in plaintext MCP configuration, protect the local configuration directory, and assume the audit database may contain sensitive CI/CD data.

Risk: Destructive maintenance actions such as artifact deletion or branch protection changes can remove data or disrupt workflows.

Mitigation: Review dry-run output before destructive actions, use explicit maintenance intent, and preserve undo or audit context where the tool provides it.

## Reference(s):

- [CICD-AIops GitHub repository](https://github.com/AIops-tools/CICD-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured CI/CD findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-result summaries, RCA findings, dry-run recommendations, audit context, and undo guidance.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
