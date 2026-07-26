## Description: <br>
Physical-device control safety gate that prevents blind cloud-device toggles by checking state, surfacing risk, and requiring explicit approval before risky actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hohobohan](https://clawhub.ai/user/hohobohan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill before controlling smart-home or cloud-connected physical devices to classify command risk, verify state, and require explicit approval for risky or irreversible actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud APIs may report success without the physical device changing state, or may push a device into an offline state. <br>
Mitigation: Read device state before and after each command, stop on ambiguous state, and require explicit approval for risky power or account-level actions. <br>
Risk: First-time or chained device-control commands can change persistent settings or require physical recovery. <br>
Mitigation: Use dry runs or non-critical devices first, execute one command at a time, and keep documented recovery procedures available. <br>
Risk: The skill is safety-oriented, but referenced device-control APIs or scripts still need their own authorization and rollback safeguards. <br>
Mitigation: Confirm approval gates, authorization controls, and recovery paths in the actual control implementation before installation or use. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/hohobohan/skills/safe-device-control) <br>
- [Dreame AP10 MiOT integration reference](https://github.com/CodyJon/dreame-ap10-integration) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis] <br>
**Output Format:** [Markdown guidance with checklists and approval gates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires state reads before and after risky device-control actions, explicit approval for write-risky actions, and typed approval for irreversible actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
