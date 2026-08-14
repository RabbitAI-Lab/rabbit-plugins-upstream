## Description:

Use when the user encounters VolcEngine errors or needs local troubleshooting for OpenAPI, Python SDK, CLI, IAM, billing, compute, networking, storage, database, CDN, media, AI, security, or VKE cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to triage VolcEngine service, API, CLI, SDK, identity, billing, networking, storage, media, AI, security, and VKE failures from local evidence. It emphasizes read-only diagnostics, minimal context collection, credential redaction, and explicit user confirmation before any sensitive or write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some reference tables can steer an agent toward retrieving secrets or running disruptive diagnostic actions.

Mitigation: Use least-privilege VolcEngine credentials, review actions before installation or execution, and require explicit user confirmation plus a redaction/no-log plan before any sensitive retrieval or disruptive diagnostic.

Risk: Troubleshooting output may expose credentials, tokens, account identifiers, billing details, object contents, kubeconfigs, or secret values if raw command output is shared.

Mitigation: Do not print SecretKey, SessionToken, full AccessKeyId, full phone numbers, bill details, object contents, kubeconfigs, or secret values; summarize only the minimum evidence needed for the current issue.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-troubleshooting)
- [Publisher profile](https://clawhub.ai/user/volc-sdk-team)
- [Skill entrypoint](artifact/SKILL.md)
- [Getting Started](artifact/references/getting-started.md)
- [OpenAPI Quick Check](artifact/references/openapi-quick-check.md)
- [Domain troubleshooting guides](artifact/references/domain-guides/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with diagnostic explanations, read-only CLI commands, and optional script snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should redact secrets, avoid raw sensitive data, and present write or disruptive actions only as proposals requiring explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata, released 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
