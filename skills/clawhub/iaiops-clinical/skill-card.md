## Description:

iaiops-clinical helps agents inspect clinical facility systems across BACnet/IP, Modbus, and OPC-UA, with patient-safety checks for isolation room pressure, medical gas pressure, and operating room environment readings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, facilities engineers, and clinical operations teams use this skill to guide agents through read-first hospital facilities diagnostics, protocol checks, patient-safety inspections, downtime triage, and configuration drafting. Its outputs are decision-support artifacts and operating guidance that require site review before use in patient-safety or OT environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags the skill as suspicious because it presents itself as read-only while documenting a high-risk BACnet write tool for clinical facilities.

Mitigation: Treat the skill as write-capable, restrict BACnet credentials and network reachability to what is explicitly needed, and require independent human approval before any write.

Risk: Outbound export and publish behavior may expose hospital facilities or OT data beyond the intended environment.

Mitigation: Restrict or disable export and publish destinations unless they are explicitly approved for the site and data class.

Risk: Use in hospital and OT environments can inherit dependency and deployment supply-chain risk.

Mitigation: Install dependencies only from pinned, verified sources in an isolated environment.

Risk: Clinical safety checks are structural analyses and may not reflect final site authority for life-safety decisions.

Mitigation: Use outputs as decision support and verify results against site procedures, NFPA 99 alarm panels, infection-control practice, and authorized facilities review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets, check results, configuration drafts, and structured analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include references to source readings, worst-first issue ordering, dry-run write guidance, and site-specific review cautions.]

## Skill Version(s):

0.28.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
