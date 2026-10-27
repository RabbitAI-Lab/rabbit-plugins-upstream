## Description:

Supports industrial teams troubleshooting discrete-manufacturing equipment through cross-protocol diagnostics, asset inventory, downtime analysis, and governed control-system changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Plant engineers and operations teams use this skill to inspect PLCs, CNC equipment, sensors, and production-line data, investigate downtime, and prepare approved changes across industrial protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved write tools can change control-system state or interrupt production.

Mitigation: Keep writes disabled or in dry-run until an authorized change-control approval is in place; review the proposed change and undo information before execution.

Risk: File and credential access may expose sensitive plant information or write outside intended locations.

Mitigation: Restrict permitted read and write directories and secret-store keys to the minimum needed for the site.

Risk: Raw-socket or root-level industrial protocol access can affect plant-network safety.

Mitigation: Run these protocol features only on dedicated plant networks with appropriate safety controls.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Text or Markdown, with configuration drafts and commands when appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first diagnostics; control-system writes require governed approval.]

## Skill Version(s):

0.32.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
