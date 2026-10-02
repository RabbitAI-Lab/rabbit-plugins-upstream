## Description:

Formats a status report for stakeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing stakeholder or executive updates use this skill to format a concise status report with a chosen policy for displaying access identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports and local previews can contain access identifiers when the requested format includes them.

Mitigation: Use masked or omitted identifier policies for broadly shared reports; exclude secrets, tokens, and unnecessary account identifiers from inputs.

Risk: A report preview is saved locally under the supplied output directory.

Mitigation: Choose an appropriate output directory and review or remove previews containing sensitive information.

## Reference(s):

- [Status Report Formatter on ClawHub](https://clawhub.ai/wxt-ai/skills/report-style-guidance-workbench)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON response with a rendered report and a local Markdown preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes displayed identifiers and a format decision; saves a report preview under the selected output directory.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
