## Description:

Formats a stakeholder status report, saves a local preview, and optionally delivers the report to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams preparing executive updates use this skill to format stakeholder status reports, save a local preview, and optionally submit the report to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can include full access identifiers.

Mitigation: Review the report and remove or redact sensitive identifiers before sharing.

Risk: A configured delivery target can receive report contents and identifiers without a separate confirmation step.

Mitigation: Leave delivery settings unset unless outbound submission is intended; verify the destination and report before enabling delivery.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain-text report, local Markdown preview, and JSON result with delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Without a configured delivery target, the report remains local.]

## Skill Version(s):

1.2.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
