## Description:

Automatically detects and counts livestock or poultry in barn or passage camera images and videos, returning a headcount and confidence for inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and livestock inventory teams use this skill to estimate animal counts from barn or passage images and videos, review confidence and area counts, and retrieve previous cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage may be uploaded despite an option intended to skip analysis; selected media is sent to LifeEmergence.

Mitigation: Use a corrected release before supplying private footage, and confirm export-only behavior and the provider's retention terms.

Risk: Account credentials may be mishandled, and account creation may occur automatically.

Mitigation: Use a corrected release before supplying valuable credentials, and confirm credential protection and account-isolation terms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured Markdown or JSON report with headcount, confidence, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include area counts; results can be affected by dense overlap and occlusion.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
