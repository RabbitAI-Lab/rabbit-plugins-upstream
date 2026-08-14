## Description:

Retrieves patent abstract images from the Zhihuiya patent database by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve abstract drawings for one or more patents by supplying patent IDs or publication numbers, then present the returned image paths and patent metadata without legal or subjective analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends patent identifiers, API keys, and related request metadata to LinkFox services.

Mitigation: Use only with patent identifiers and credentials that are appropriate to share with LinkFox, and confirm endpoint environment variables before execution.

Risk: Authentication recovery may involve phone numbers, SMS codes, and API-key generation.

Mitigation: Prefer self-service key setup where possible, avoid sharing one-time codes in chat, and rotate or revoke generated API keys if they were exposed.

Risk: Billing flows can create paid credit orders and the lookup itself consumes credits based on returned results.

Mitigation: Confirm costs and payment method with the user before creating orders or running additional lookups.

Risk: Lookup results and cached responses can be saved locally under a LinkFox workspace directory.

Mitigation: Treat saved response files as retained data, review them before sharing, and remove local history when it is no longer needed.

Risk: The skill can automatically report feedback about behavior or user sentiment to the LinkFox feedback endpoint.

Mitigation: Avoid including sensitive user content in feedback and disclose that feedback may be sent when reporting issues or praise.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-image)
- [智慧芽-摘要附图 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with image links, JSON API responses, and saved JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires patentId or patentNumber; supports up to 100 comma-separated identifiers per request; responses may be cached locally for 24 hours.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
