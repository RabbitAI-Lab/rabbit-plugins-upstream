## Description:

Helps agents analyze how a brand's popular Shopee products are distributed across subcategories, ordered by sales over the past 30 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market analysts use this skill to examine a brand's Shopee product mix and identify its leading subcategories for a selected site, category, and date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and Node, changing the local environment.

Mitigation: Prefer a user-installed, pinned qhkit version and require explicit approval before any installation, download, or upgrade.

Risk: Entering an API token in chat or a shell command can expose the credential.

Mitigation: Keep tokens out of chat and command history; use a secure configuration or environment variable.

Risk: Qinghu API requests consume paid credits, and failed requests may still incur charges.

Mitigation: Check the current estimate and obtain explicit approval before paid calls; limit retries and report actual credit use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-categories)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Analysis, Text, Files]

**Output Format:** [Concise Markdown findings; a table file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings identify platform, site, period, sample size, and credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
