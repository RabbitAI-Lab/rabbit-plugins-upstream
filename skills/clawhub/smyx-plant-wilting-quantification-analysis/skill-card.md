## Description:

Analyzes plant images or video to estimate wilting severity and suggest whether underwatering or overwatering may be responsible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, greenhouse operators, and developers can assess wilting from plant images or video, review possible watering-related causes, and retrieve historical reports. Soil-moisture information, when available, can help distinguish underwatering from overwatering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent identities and service tokens in a shared workspace can expose account data or report history across users.

Mitigation: Install only in a single-user or tightly isolated workspace until identity isolation is fixed; protect local workspace data and tokens.

Risk: Plant media or media URLs are sent to an external service, and report history is fetched from the cloud.

Mitigation: Inform users of cloud processing and avoid submitting sensitive images or URLs without authorization.

Risk: Visual symptoms alone may not reliably distinguish underwatering from overwatering.

Mitigation: Check soil moisture before acting on watering or drainage advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Plant wilting API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or JSON result; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link and watering or drainage guidance.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
