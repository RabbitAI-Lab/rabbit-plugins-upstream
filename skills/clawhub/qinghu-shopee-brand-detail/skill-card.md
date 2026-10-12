## Description:

Retrieves Shopee brand product counts, sales, revenue, and shop counts for up to 10 brand names per query.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market analysts use this skill to compare Shopee brands by product count, sales, revenue, and shop count across supported sites and reporting dates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests runtime installation or upgrades to perform a brand query.

Mitigation: Review before installing and prefer a preinstalled, version-pinned qhkit.

Risk: The skill may persist API credentials on the host.

Mitigation: Use a session-scoped QHKIT_TOKEN instead of writing persistent credentials.

Risk: Brand-data calls spend Qinghu credits.

Mitigation: Confirm the estimated credits and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-detail)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Brief written summaries; spreadsheet files for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 10 brands per query; paid calls require prior user approval.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
