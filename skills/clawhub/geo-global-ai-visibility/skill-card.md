## Description:

Checks whether overseas brands appear in responses from major AI platforms and summarizes rankings, competitor mentions, and cited websites in a shareable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hclscut](https://clawhub.ai/user/hclscut)

### License/Terms of Use:

MIT-0

## Use Case:

External brand and marketing teams use this skill to check how AI platforms answer market-specific product questions and see whether and where their brands appear. It summarizes competitor mentions and citations, then can produce a shareable HTML report with practical visibility suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says setup guidance asks users to share an API key in chat, which could expose the credential.

Mitigation: Keep the API key private and configure it locally; do not paste it into chat.

Risk: The security review flags broad activation guidance that may prompt use outside a relevant brand visibility check.

Mitigation: Use the skill for an explicit visibility check and review the planned questions and platforms before submitting.

Risk: The security review reports an unresolved concern about environment data reaching a network request.

Mitigation: Review the network behavior and limit sensitive environment data before running the skill.

## Reference(s):

- [MaxAEO Developer Documentation](https://maxaeo.cn/docs/developers/)
- [ClawHub Skill Page](https://clawhub.ai/hclscut/skills/geo-global-ai-visibility)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance]

**Output Format:** [Text summary and shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include platform responses, brand and competitor visibility, and cited websites when available.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
