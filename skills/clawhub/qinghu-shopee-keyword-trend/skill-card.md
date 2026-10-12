## Description:

Queries up to 30 days of daily sales, revenue, and search-interest trends for a Shopee hot keyword ID through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts use this skill to assess a keyword's recent daily sales, revenue, and search-interest trends across supported Shopee sites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install or update software, including optional Node.js bootstrapping.

Mitigation: Review before use; prefer a host-managed, pinned qhkit installation and avoid automatic Node/npm bootstrapping.

Risk: Configuring Qinghu access may persist an API credential locally.

Mitigation: Use a scoped token through a secure secret mechanism instead of persistent local configuration where possible.

Risk: Trend lookups can incur paid Qinghu API charges.

Mitigation: Check available pricing and obtain user approval before paid calls; report actual credits charged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-keyword-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise trend analysis in text or Markdown, with a table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the site, date range, and charged Qinghu credits for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
