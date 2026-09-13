## Description:

CICD AIops helps agents inspect and operate self-managed GitLab and self-hosted Gitea CI/CD servers, including pipelines, runners, artifacts, repository hygiene, RCA workflows, and governed write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD operators use this skill to diagnose failed pipelines, runner capacity, artifact storage, stale work, and branch protections on self-managed GitLab or self-hosted Gitea instances. They can use its CLI or MCP tools to prepare or execute governed remediation while preserving audit records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs external code without trusted provenance recorded for this version.

Mitigation: Review before installing and use an exact pinned package version or trusted provenance when deploying.

Risk: The skill can perform high-impact GitLab or Gitea changes, including irreversible artifact deletion and branch-protection changes.

Mitigation: Use a read-only or narrowly scoped token by default and require an explicit local approval process before live writes.

Risk: Providing the master password directly in MCP configuration can expose sensitive credentials through client configuration handling.

Mitigation: Avoid storing the master password directly in MCP config where possible and prefer environment handling appropriate to the deployment.

Risk: Some platform surfaces are GitLab-only or have incomplete storage visibility on Gitea, which can lead to misleading conclusions if ignored.

Mitigation: Check platform support labels, truncation indicators, and null fields before interpreting runner, pipeline, artifact, or storage results.

## Reference(s):

- [CICD-AIops GitHub repository](https://github.com/AIops-tools/CICD-AIops)
- [cicd-aiops ClawHub listing](https://clawhub.ai/zw008/skills/cicd-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Analysis]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CI/CD RCA findings, command recommendations, configuration snippets, and risk notes for governed write operations.]

## Skill Version(s):

0.10.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
