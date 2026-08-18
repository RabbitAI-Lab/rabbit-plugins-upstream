## Description:

Retrieves patent description and specification content from the Zhihuiya patent database by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve full patent specifications for one or more known patent IDs or publication numbers, including optional family-member substitution when the requested description is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries, reusable API keys, and full patent responses are handled by LinkFox services.

Mitigation: Use the skill only for data suitable for LinkFox processing, manage API keys as secrets, and avoid sensitive projects unless service handling is approved.

Risk: Full patent responses and cached query results are stored locally under linkfox directories.

Mitigation: Control access to the workspace and linkfox data directories, and delete response or cache files when retention is not appropriate.

Risk: The skill includes automatic feedback reporting and environment-variable endpoint overrides.

Mitigation: Disable or tightly control feedback submission and endpoint override variables before use in sensitive environments.

Risk: Authentication recovery and billing flows can involve phone-based onboarding, reusable API keys, and paid credit purchases.

Mitigation: Review onboarding and billing steps before execution, require explicit user confirmation for purchases, and avoid exposing generated API keys in logs or shared terminals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files or summarized in stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full patent responses under a local linkfox session data directory; responses larger than 8 KB are summarized unless inline output is requested; query results are cached for 24 hours by parameter set.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
