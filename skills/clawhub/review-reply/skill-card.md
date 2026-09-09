## Description:

Helps Amazon sellers triage subscribed ASIN negative reviews and generate AI-drafted buyer replies, platform appeal suggestions, product improvement ideas, and review handling status updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to review pending negative feedback, draft buyer communication and appeal language, and convert review themes into product or listing improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits or change monitoring and billing-related behavior with too much automatic authority.

Mitigation: Use an ask-before-spending posture, keep autoconfirm limits conservative or disabled, and review any request to enable monitoring, add competitors, export files, or change confirmation settings.

Risk: The skill sends Amazon review and account-related workflow data to ARI services.

Mitigation: Install only if the user trusts ARI/funewa with the relevant Amazon review data and understands that ARI API access is required.

Risk: Custom API base URLs could redirect credential-bearing requests away from the official ARI service.

Mitigation: Avoid enabling custom API base URLs unless the destination is a trusted, user-controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-reply)
- [ARI user guide](使用说明.md)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text responses, with JSON returned by the ARI CLI and optional CSV, Markdown, or HTML export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may use ARI credits for collection, analysis, monitoring, reports, or exports depending on the requested workflow.]

## Skill Version(s):

1.4.8 (source: server release, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
