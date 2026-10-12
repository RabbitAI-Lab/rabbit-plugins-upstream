## Description:

Retrieves Ozon keyword metrics by keyword ID, including search, conversion, exposure, supply-demand, and order-value indicators for up to 10 keywords per request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to compare Ozon keyword demand and competition metrics for product and search planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt installation or upgrades of external tooling and changes to the local environment.

Mitigation: Preinstall a pinned, trusted qhkit version and approve any host changes before use.

Risk: Configuring the Qinghu API token on the host can expose or persist credentials.

Mitigation: Provide a scoped secret or temporary environment variable instead of storing the token on the host.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-keyword-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Ozon reporting period and keyword IDs; up to 10 IDs per query.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
