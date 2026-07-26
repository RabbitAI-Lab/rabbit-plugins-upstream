## Description: <br>
PagerDuty skill for reading incident and on-call data and updating incident state through the OOMOL oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, incident responders, and operations teams use this skill to inspect PagerDuty schemas, retrieve incidents and on-call assignments, and perform confirmed incident state changes through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change PagerDuty incident state through acknowledge, resolve, and update actions. <br>
Mitigation: Confirm the exact incident, action, and payload with the user before running write actions. <br>
Risk: PagerDuty operations are routed through the OOMOL oo CLI and server-side credential handling. <br>
Mitigation: Install and use the skill only when the user trusts OOMOL and intends to operate through an OOMOL-connected PagerDuty account. <br>
Risk: Connector schemas may define required fields or effects that are not visible from the skill summary alone. <br>
Mitigation: Inspect the live connector schema before constructing command payloads. <br>


## Reference(s): <br>
- [ClawHub PagerDuty skill page](https://clawhub.ai/oomol/skills/oo-pagerduty) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [PagerDuty homepage](https://www.pagerduty.com) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PagerDuty connector JSON responses when commands are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
