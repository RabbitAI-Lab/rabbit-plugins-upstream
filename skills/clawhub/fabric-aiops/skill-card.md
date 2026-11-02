## Description:

Operate network-fabric controller APIs to assess health, analyze connectivity and configuration, and perform audited changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Network operators and engineers use this skill to inspect network and device health, analyze WAN uplinks and Cisco ACI endpoint paths, and manage supported controller resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Controller tools can make disruptive network changes without requiring human approval.

Mitigation: Start with a read-only controller account. Before enabling writes, require approval for the exact operation, target, and parameters; test in a lab, check audit warnings and health, and account for reboots having no undo.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops)
- [Capabilities reference](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON results and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Controller coverage varies by platform; live controller verification is incomplete.]

## Skill Version(s):

0.15.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
