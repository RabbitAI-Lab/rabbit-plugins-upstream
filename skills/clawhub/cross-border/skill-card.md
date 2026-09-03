## Description:

This skill helps cross-border ecommerce operators collect and compare Amazon reviews across eight marketplaces to identify local complaints, consumer signals, localization needs, and listing or product improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and marketplace teams use this skill to analyze Amazon ASIN review data across supported regional sites, generate VOC and consumer insight reports, compare competitors, monitor reviews, and prioritize listing or product changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI actions can spend credits for reports or paid data workflows, and auto-confirm behavior may allow small paid actions without a separate prompt.

Mitigation: Keep autoconfirm off or require explicit approval for paid commands; review credit estimates and autoConfirm notes before generation.

Risk: The skill stores an ARI API key locally and sends authorized requests to the ARI service.

Mitigation: Use the documented local configuration or ARI_API_KEY path only, keep the key out of reports and public materials, and revoke keys that may have been exposed.

Risk: Monitoring, schedule, competitor, and account preference commands can alter recurring collection or account automation.

Mitigation: Confirm the intended account change, frequency, and expected recurring cost before running management commands.

Risk: Exports can create local CSV, Markdown, or HTML files containing review or report data.

Mitigation: Create exports only when requested and handle generated files as business data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/cross-border)
- [README](artifact/README.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON CLI responses, shell commands, and exported CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; some analysis, collection, category, and advice workflows may consume ARI credits or change ongoing monitoring preferences.]

## Skill Version(s):

1.4.5 (source: server release evidence, _meta.json, SKILL.md frontmatter, and CLI VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
