## Description:

Amazon 消费者预期差距 checks Amazon product-page promises against real customer review experience for evidence-based promise audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare listing claims with collected review evidence before making product, listing, or monitoring decisions. It is not intended for legal compliance review, unsupported marketing copy, or brand strategy without product and review data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI account credits under the user's account confirmation rules.

Mitigation: Use quote-only flows before paid actions when requested, turn autoconfirm off when every paid action should require confirmation, and review credit estimates before approving execution.

Risk: ARI API keys authorize account activity and could be exposed if copied into reports, prompts, or command examples.

Mitigation: Use browser setup or local configuration, keep keys out of generated reports and examples, and avoid untrusted ARI_BASE_URL or ARI_ALLOW_CUSTOM_BASE settings.

Risk: Monitoring, competitor tracking, exports, or workbench status changes can alter ongoing account state or future collection behavior.

Mitigation: Confirm the exact requested change and any stated cost before enabling weekly or daily monitoring, competitor tracking, exports, or workbench status updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/customer-gap)
- [Usage instructions](artifact/使用说明.md)
- [Dedicated operations workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise text guidance with optional JSON or CLI command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, review sample counts, data-window notes, credits used, and account-balance information when returned by ARI.]

## Skill Version(s):

1.4.7 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
