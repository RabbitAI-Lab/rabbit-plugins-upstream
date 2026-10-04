## Description:

Guides developers in sealing Python workflows into locally delivered packages that run on authorized customer nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zkeviny](https://clawhub.ai/user/zkeviny)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vendors use this skill to package and license Python scripts or automation workflows for local, node-authorized customer delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sealed packages hide their source and may perform local file or subprocess operations.

Mitigation: Accept packages only from trusted providers and run them in a restricted account or sandbox.

Risk: Copying a local MGC authentication token into scripts can expose the token.

Mitigation: Avoid embedding raw tokens in scripts; prefer official MGC tool calls when possible.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zkeviny/skills/seal-and-license-workflow-skills)
- [MGC Blackbox project documentation](https://github.com/zkeviny/MGC-Blackbox)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Python and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local packaging, customer-key sealing, import, and execution.]

## Skill Version(s):

1.2.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
