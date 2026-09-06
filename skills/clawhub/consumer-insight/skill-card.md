## Description:

Generates Amazon consumer insight reports that connect review evidence to customer profiles, purchase motivations, use cases, pain points, competitive alternatives, and product improvement opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and market researchers use this skill to analyze ASIN review data, generate VOC and consumer insight reports, monitor negative-review alerts, compare competitors, and export reports or review data. It requires an ARI API key and may perform paid ARI credit operations when confirmed or when server-side auto-confirm applies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI credits may be spent through server-side auto-confirm behavior without fresh approval for each paid action.

Mitigation: Review the auto-confirm behavior before installation, consider setting autoconfirm off, and allow paid reports, schedules, watch actions, or competitor actions only when clearly requested.

Risk: ARI credentials can authorize account access and paid operations for the configured account.

Mitigation: Configure credentials only for the intended ARI account, keep API keys out of prompts, reports, examples, screenshots, and public files, and rotate the key if it is exposed.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/consumer-insight)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports, structured JSON command responses, shell commands, and exported Markdown, HTML, or CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include report links, report IDs, credit usage, account balance context, and local export paths when returned by ARI.]

## Skill Version(s):

1.4.5 (source: server release evidence, skill frontmatter, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
