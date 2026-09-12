## Description:

CICD AIops helps agents inspect, troubleshoot, and perform governed operations on self-managed GitLab and self-hosted Gitea CI/CD servers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect CI/CD server state, diagnose failed pipelines, runner capacity, artifact storage, and stale repository work, then perform governed remediation actions when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact GitLab or Gitea changes without built-in read-only or approval enforcement.

Mitigation: Use read-only or narrowly scoped tokens by default, reserve write or admin-capable tokens for specific tasks, and review every write before execution.

Risk: Destructive CI/CD operations can delete artifacts or otherwise change server state.

Mitigation: Run destructive actions only after a dry-run preview, require a clear operator rationale, and avoid broad deletion scopes unless the preview matches the intended maintenance window.

Risk: Credential handling can expose the master password if it is placed in shared, synced, or source-controlled MCP configuration.

Mitigation: Keep the master password out of shared files and source control, and provide it through local secret management or narrowly scoped runtime environment injection.

## Reference(s):

- [CICD-AIops GitHub repository](https://github.com/AIops-tools/CICD-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and structured operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CI/CD RCA findings, dry-run recommendations, audit guidance, and platform-specific limitations.]

## Skill Version(s):

0.10.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
