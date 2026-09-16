## Description:

iaiops-factory helps agents support discrete-manufacturing diagnostics and troubleshooting across PLC, CNC, fieldbus, MQTT/Sparkplug, UNS, OEE, asset inventory, and downtime root-cause workflows, with read-first behavior and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and manufacturing engineers use this skill to guide agents through factory connectivity, tag discovery, health checks, OEE and downtime analysis, asset inventory, and controlled production-line troubleshooting. The skill is intended for read-first workflows, with write-capable actions treated as high-risk and gated by management-of-change approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers powerful factory and OT diagnostics, including workflows that may involve write-capable industrial actions or elevated network access.

Mitigation: Keep write tools in dry-run until formal MOC approval, review commands before production use, and grant CAP_NET_RAW or root only to the smallest necessary component.

Risk: Unpinned or unreviewed dependencies and broad runtime access can increase operational risk in a production plant environment.

Mitigation: Review and pin the iaiops package and dependencies, install in an isolated environment, and keep API tokens in the documented secret store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-factory)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline commands, configuration details, and tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing operational guidance for industrial diagnostics; write workflows require review and approval before production use.]

## Skill Version(s):

0.28.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
