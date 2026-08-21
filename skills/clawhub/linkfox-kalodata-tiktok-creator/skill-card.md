## Description:

Searches Kalodata TikTok Shop creator leaderboards and retrieves selected creator profiles, sales metrics, video and live performance, contact channels, and related shop information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce analysts use this skill to discover high-performing TikTok Shop creators by region, date range, language, and currency, then inspect a selected creator's performance and contact details by creatorId.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an API key and spends LinkFox/Kalodata credits for each lookup.

Mitigation: Confirm credential setup and expected credit use before repeated searches or pagination.

Risk: Creator results, including possible contact fields, are stored locally as full response files.

Mitigation: Review local persistence behavior and avoid running the skill in workspaces where creator contact data or private prompts should not be retained.

Risk: The skill includes onboarding and billing flows that can guide account setup and create unpaid payment orders or QR codes.

Mitigation: Use billing commands only after explicit user approval and verify plan, payment method, and order details before proceeding.

Risk: The skill can automatically submit feedback content to LinkFox.

Mitigation: Review or disable feedback behavior when user prompts or creator data may be sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-creator)
- [Kalodata creator API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, and shell commands for scripted lookups or onboarding.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are persisted locally; small responses may be printed in full, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
