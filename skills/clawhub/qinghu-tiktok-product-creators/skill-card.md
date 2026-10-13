## Description:

Finds TikTok creators who have promoted a product using its product ID through Qinghu's data tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to find TikTok creators associated with a specified product for competitor research or outreach planning. Creator details require a separate lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends installing or upgrading qhkit, including unpinned executions.

Mitigation: Review the dependency before installation and prefer a preinstalled, pinned qhkit version over unpinned npx or @latest execution.

Risk: Configuring a Qinghu API token may expose credentials if pasted into shell commands or persistent configuration.

Mitigation: Use a scoped token through a secure environment mechanism and confirm how any persistent configuration stores it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-creators)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary with optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paged creator list; creator details need a separate query. Reports credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
