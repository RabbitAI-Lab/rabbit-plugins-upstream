## Description:

Guides data analysts in using MGC Blackbox to manage local credentials, scripts, workflows, knowledge, and sealed collaboration with explicit approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Data analysts and developers use this skill to manage local credentials, user-owned analysis workflows, knowledge, and authorized sharing through MGC Blackbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-triggered credential access or workflow execution can perform sensitive operations.

Mitigation: Require explicit user approval for each sensitive operation.

Risk: The MGC token or retrieved credentials can be exposed.

Mitigation: Treat the token and any retrieved credential content as secrets.

Risk: Broad zero-exposure claims may overstate protection for knowledge or script internals.

Mitigation: Do not assume those contents are invisible to the agent; review what each operation reveals.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zkeviny/skills/mgc-database-security)
- [MGC Blackbox project](https://github.com/zkeviny/MGC-Blackbox)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with code examples and tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MGC Blackbox 1.5.2+ for the documented workflows.]

## Skill Version(s):

1.3.0 (source: ClawHub release and bundled skill)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
