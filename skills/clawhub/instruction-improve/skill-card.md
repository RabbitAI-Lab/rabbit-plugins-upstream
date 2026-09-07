## Description:

Analyzes Amazon review questions about installation, use, and maintenance to identify evidence-backed improvements for product instructions; it does not provide medical, legal, safety-certification, or automatic publishing decisions and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to turn account-linked Amazon review data into instruction-improvement priorities and supporting evidence for product documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access account-linked Amazon review data through an ARI API key.

Mitigation: Use a dedicated ARI API key, do not paste credentials into chat or reports, and revoke or recreate the key from the publisher account page if needed.

Risk: Some ARI analysis actions may spend credits automatically under the account's auto-confirm policy.

Mitigation: Use 'only quote, do not execute' or set auto-confirm off before analysis when every paid action needs a fresh approval.

Risk: Paid analysis or collection may complete after a network interruption, so immediate retry can duplicate spending.

Mitigation: Check existing reports or operation status using the original request ID before retrying confirmed paid actions.

Risk: The skill can change persistent ARI settings such as auto-confirm rules and monitoring schedules.

Mitigation: Require explicit user intent for settings changes and restate the active rule or estimated ongoing cost after changes.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Amazon 使用说明改进 专属运营工作流](references/operation-workflow.md)
- [ARI Amazon 评论智能助手使用指南](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/instruction-improve)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese-language Markdown or text responses, with shell command snippets and JSON-derived status details when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, export file paths, account status, credits used, quote details, and confirmation requirements returned by ARI.]

## Skill Version(s):

1.4.7 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
