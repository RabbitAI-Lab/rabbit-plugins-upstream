## Description:

Analyzes Chinese security and intelligent-building tenders using historical procurement data to recommend whether to bid, identify likely competitors, estimate a bid range, and flag qualification risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams and contractors evaluating a specific security or intelligent-building tender use this skill to assess procurement history, competition, indicative pricing, and bid eligibility before deciding whether to participate.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: First-time use may create an account and store an API key on the user's device.

Mitigation: Obtain consent before registration, use an existing key when available, and protect the locally stored credential.

Risk: Saved or shared reports may expose signed source links that bypass login.

Mitigation: Review reports before sharing, restrict access to saved HTML and intermediate JSON, and avoid broadly forwarding signed links.

Risk: Bid-data queries consume account credits.

Mitigation: Disclose expected credit use before analysis and obtain approval before exceeding the planned query budget.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dragonzu/skills/intelligent-building-bid-decision)
- [Analysis workflow](references/workflow.md)
- [API quick reference](references/api-quick.md)
- [Report template](references/report-template.md)
- [Account setup reference](references/auto-register.md)
- [Skill setup documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Markdown, HTML files]

**Output Format:** [Markdown decision report in chat and a saved HTML report in full mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites supporting records and provides a bid recommendation and indicative price range; saved reports can contain signed source links.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
