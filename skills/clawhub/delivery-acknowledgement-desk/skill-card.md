## Description:

Sets delivery acknowledgement guidance and creates a local delivery acknowledgement receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams handling deliveries use this skill to derive acknowledgement guidance from a delivery profile and, when requested, create a local confirmation receipt using that guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream operation writes receipt files to the chosen output directory.

Mitigation: Supply your own request JSON and use a dedicated, writable output directory.

Risk: A local receipt could be mistaken for confirmation of an external delivery.

Mitigation: Treat the receipt as a local record; verify external delivery separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/delivery-acknowledgement-desk)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON output with acknowledgement guidance or a confirmation result; optional local receipt file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes a local receipt only when given an output directory; it does not confirm an external delivery.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
