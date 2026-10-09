## Description:

Helps agents query and summarize Ozon brand rankings by category, brand, and reporting period, sorted by sales volume, revenue, or price.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and market analysts use this skill to compare top brands within a category or reporting period and review sales rankings before making commercial decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or upgrading of mutable Node and qhkit packages can run external software and modify the local environment.

Mitigation: Preinstall a trusted, pinned qhkit version; require approval before global installs, npm or npx execution, PATH changes, or shell-profile edits.

Risk: Access to paid Qinghu data requires an API token, and ranking queries may incur variable credit charges.

Mitigation: Configure the token through a trusted channel, check the current estimate, and confirm paid calls and large result requests before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-ozon-brand-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise ranking summary with key figures and, for larger results, a tabular file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on selected category, brand, reporting period, sort order, and page size; paid calls report consumed credits.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
