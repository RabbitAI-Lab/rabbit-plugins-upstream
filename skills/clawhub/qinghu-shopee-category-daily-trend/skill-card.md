## Description:

Queries daily Shopee category sales volume and revenue trends by category ID for up to 720 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to review daily category sales and revenue trends for a selected marketplace, category, and date range.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or upgrade Node and an unpinned qhkit CLI, changing the user's environment beyond the query.

Mitigation: Request approval before setup changes; prefer a reviewed, preinstalled qhkit version instead of @latest or npx execution.

Risk: Configuring qhkit may store a Qinghu API token on the user's machine.

Mitigation: Obtain user confirmation before configuring the token and avoid exposing it in responses.

Risk: Category data requests can incur Qinghu credits.

Mitigation: Explain expected charges and obtain user consent before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-daily-trend)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend summary with supporting figures; a table file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports marketplace, date range, and sample size; paid calls require user consent.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
