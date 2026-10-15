## Description:

Queries Shopee category sales, revenue, and product counts for a chosen site, date, and category level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts compare category size across a supported site and reporting date using sales, revenue, and product-count data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrades of Node and qhkit can change the user's environment, including shell startup files.

Mitigation: Install a trusted, pinned qhkit version yourself and avoid automatic changes to shell startup files.

Risk: The skill requires a qhkit token and may make paid data calls.

Mitigation: Configure the token securely; review estimated credits and approve the requested calls before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-list)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise findings with supporting metrics; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the Shopee site, reporting date, sample size, and credits used for paid calls.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
