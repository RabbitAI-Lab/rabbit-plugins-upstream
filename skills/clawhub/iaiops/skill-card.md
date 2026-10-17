## Description:

Routes industrial and operational-technology troubleshooting tasks to the appropriate iaiops edition and MCP profile, with read-first guidance for device access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial engineers and operations teams use this skill to select an edition for their site, assess setup and readiness, and plan read-first troubleshooting across industrial protocols. Device writes require site authorization and explicit safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device writes can change industrial processes or equipment state.

Mitigation: Keep connections read-only until authorized by the site; use the documented dry-run, named approval, and double-confirmation controls before any real write.

Risk: The router relies on separate edition skills and an MCP server that are not included in this artifact.

Mitigation: Review the linked edition skills and MCP server/package before connecting to real industrial systems.

Risk: Incorrectly assigning tag roles can produce plausible but misleading operational metrics.

Mitigation: Have site personnel supply tag semantics; do not guess roles or fill uncertain endpoint configuration fields.

## Reference(s):

- [iaiops release on ClawHub](https://clawhub.ai/zw008/skills/iaiops)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to separate edition skills and an MCP server; does not itself provide a tool inventory.]

## Skill Version(s):

0.29.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
