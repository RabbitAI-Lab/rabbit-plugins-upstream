## Description:

Looks up Shopee top-level category IDs and names by marketplace site and language using 青虎AI data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts use this skill to find top-level category IDs and names for a chosen marketplace and language before making category-based queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can install or upgrade tooling on the user's machine for a small lookup task.

Mitigation: Review setup before execution; install in a disposable or managed environment, pin the qhkit version, and avoid global upgrades.

Risk: Configuring an API token locally can expose or persist credentials.

Mitigation: Supply the qhkit token through a controlled secret mechanism rather than saving it locally.

Risk: Category lookups use a paid tool and may consume credits.

Mitigation: Get user consent for estimated charges before paid calls and report actual credits used.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-l1)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Brief answer with category IDs and names; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are scoped to the selected Shopee site and language; paid calls report credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
