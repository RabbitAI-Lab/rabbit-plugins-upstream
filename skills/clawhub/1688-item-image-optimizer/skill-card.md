## Description:

Provides a unified workflow for 1688 product image creation, including main image optimization, carousel images, detail images, background replacement, and digital model routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External 1688/OpenClaw merchants use this skill to route product-image requests to the correct 1688 image tool, pass eligible uploaded image URLs, check digital model permission, and open the generated tool page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expects a 1688/OpenClaw AK and may use the active session to open 1688 image tools.

Mitigation: Install only if the publisher is trusted, configure credentials through the expected OpenClaw path, and verify the gateway URL before running configure.

Risk: CLI command execution sends signed usage metadata and generated tool URLs may include a local session identifier.

Mitigation: Review telemetry and session handling before deployment, and use the skill only in account contexts where this reporting is acceptable.

## Reference(s):

- [Interaction component specifications](references/interaction-specs.md)
- [ClawHub skill page](https://clawhub.ai/1688aiinfra/skills/1688-item-image-optimizer)
- [1688 image tool entry point](https://air.1688.com/app/CSBC-modules/csbc-ai-component-loader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON CLI responses with markdown text and OpenClaw interaction payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return open_tab or card interaction data for the host agent to display.]

## Skill Version(s):

0.51.0 (source: server release metadata; artifact frontmatter declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
