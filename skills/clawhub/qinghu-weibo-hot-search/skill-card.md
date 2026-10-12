## Description:

Helps agents retrieve and summarize the current Weibo hot-search rankings through Qinghu's paid data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

People tracking Weibo trends use this skill to request current hot-search rankings and receive a concise summary or tabular export of the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid lookups may incur variable charges, including for some failed calls.

Mitigation: Estimate credits and obtain user consent before calling; disclose actual credits charged.

Risk: A persistent Qinghu API token may be stored or exposed during setup.

Mitigation: Supply credentials through a secure secret manager and avoid displaying or embedding the token.

Risk: Automatic installation or upgrades modify the local Node/npm environment.

Mitigation: Prefer a preinstalled, pinned qhkit version and review changes before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-weibo-hot-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise answer with optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports paid-call credit usage and identifies the data scope.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
