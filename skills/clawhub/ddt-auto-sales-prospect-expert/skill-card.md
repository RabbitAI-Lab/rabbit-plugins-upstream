## Description:

This skill helps auto-service sales teams identify and prioritize automotive aftermarket stores for outreach using brand coverage, service type, location profile, and nearby competitor signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External sales representatives, regional managers, and channel development teams use this skill to find target auto-service stores, compare store networks, and prepare store visits for lubricants, tires, and automotive products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party DDT automotive prospecting API and may return incomplete or unavailable coverage for a requested brand, store, or area.

Mitigation: Check API success, coverage, and truncation fields before drawing business conclusions, and mark missing coverage as unavailable rather than interpreting it as zero.

Risk: The skill requires a DDT API key and may involve location coordinates or public store IDs.

Mitigation: Keep the API key in a controlled environment variable, do not paste credentials into chat or project files, and provide coordinates or store IDs only when needed for the task.

## Reference(s):

- [DDT automotive prospecting API homepage](https://gotoshop-ai.com/ddtclaw/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured recommendations and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should use only published API response data, indicate coverage gaps, avoid exposing API keys or internal fields, and limit specific store details to user-requested previews.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
