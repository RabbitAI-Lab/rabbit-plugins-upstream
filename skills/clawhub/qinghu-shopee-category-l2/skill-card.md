## Description:

Looks up Shopee second-level category IDs and names by first-level category ID, site, and language using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers, analysts, and their agents use this skill to find second-level category IDs and names for a selected marketplace site and language before filtering or drilling into category data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node tooling can change the local environment.

Mitigation: Preinstall a vetted, pinned qhkit version and approve any local installation or environment changes before use.

Risk: Configuring a Qinghu API token places a credential on the machine.

Mitigation: Require explicit approval before configuring the token and handle it as a secret.

Risk: Category lookups and related tool calls can consume paid Qinghu credits.

Mitigation: Present estimated charges and obtain explicit user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-l2)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise category lookup results; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes category IDs and names, relevant site and language, and credits spent when paid calls are made.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
