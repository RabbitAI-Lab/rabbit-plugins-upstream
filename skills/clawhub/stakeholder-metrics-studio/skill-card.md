## Description:

Calculates a metric trend from supplied CSV data and builds a stakeholder digest with a local HTML artifact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and stakeholders use this skill to summarize supplied metric series and create a local HTML digest for reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream digest writes metric data to a local HTML file, which could expose sensitive reporting data if stored in an unsuitable location.

Mitigation: Choose a dedicated output directory and review the generated HTML before sharing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/stakeholder-metrics-studio)
- [Skill usage guide](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON metric summary or digest containing HTML; optional local HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes the HTML digest beneath the selected output directory and returns an effect receipt.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
