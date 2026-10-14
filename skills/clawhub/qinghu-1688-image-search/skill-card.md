## Description:

Given public product image URLs, this skill finds matching or similar 1688 listings and summarizes suppliers, prices, and sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sourcing teams and merchants use a public product image URL to find similar 1688 products and compare supplier, price, and sales information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install Node/npm or qhkit and change PATH or shell startup settings.

Mitigation: Review installation and shell changes first; prefer a preinstalled, pinned qhkit version.

Risk: Searches use a Qinghu API token and can incur charges in credits.

Mitigation: Keep the token in a managed secret store, check the current cost estimate, and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-1688-image-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings with optional table file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits consumed for paid searches; image URLs must be publicly accessible.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
