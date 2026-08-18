## Description:

This skill retrieves recent Amazon seller policy and regulation updates, supports marketplace and date-range filtering, and fetches full article text by record ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce operators use this skill to review Amazon seller policy updates, scan AI-generated Chinese summaries, and retrieve full source article bodies for compliance awareness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API credentials and allows custom endpoint environment variables.

Mitigation: Use credentials only from the official LinkFox onboarding flow and avoid custom endpoint overrides unless the destination is fully trusted.

Risk: The skill may trigger paid-credit consumption and billing flows.

Mitigation: Warn users before repeated calls or purchases, and require user confirmation before continuing when credit cost or billing status is unclear.

Risk: The skill saves full API responses and cache files locally.

Mitigation: Review saved response files for sensitive content and manage retention according to the workspace's data-handling policy.

Risk: Security evidence rates the release suspicious because account login, API-key generation, billing, persistence, and automatic feedback behavior exceed a narrow policy-feed function.

Mitigation: Review the skill carefully before installing and limit use to environments where those behaviors are acceptable.

## Reference(s):

- [API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-policy-feed)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON responses, with saved JSON files for full API responses and concise summaries for large results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [List responses include titles, AI-generated Chinese summaries, original URLs, publish times, and record IDs; detail responses include full article Markdown.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
