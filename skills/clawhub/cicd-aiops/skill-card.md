## Description:

Governed CI/CD operations for self-managed GitLab and self-hosted Gitea, covering pipelines, runners, artifacts, RCA workflows, and audited write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI/CD operators use this skill to inspect and troubleshoot self-managed GitLab or Gitea servers, run RCA workflows, and perform audited maintenance actions such as retrying pipelines, pausing runners, changing branch protection, or deleting old artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact writes on GitLab or Gitea while its governance is primarily audit and visibility rather than authorization.

Mitigation: Use a read-only or least-privilege token by default, and require out-of-band approval before enabling write or admin scopes.

Risk: Artifact deletion is irreversible and audit records cannot restore deleted artifacts.

Mitigation: Run dry-run previews first, use conservative age filters, and require explicit approval before deleting artifacts.

Risk: Master passwords or credentials placed in synced or broadly readable MCP configuration can expose access to CI/CD servers.

Mitigation: Keep secrets out of shared configuration files, restrict file permissions, and prefer narrowly scoped tokens.

Risk: Some operations are platform-specific, so unsupported Gitea surfaces or unknown storage values can be misread as empty results.

Mitigation: Confirm the configured platform before acting and treat teaching errors, null values, and unknown byte counts as capability limits rather than clean results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/cicd-aiops)
- [Project Homepage](https://github.com/AIops-tools/CICD-AIops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI examples and structured tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CI/CD RCA summaries, command proposals, and governed write requests.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
