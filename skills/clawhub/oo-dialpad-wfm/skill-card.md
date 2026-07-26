## Description: <br>
Dialpad WFM helps agents work with Dialpad workforce management data through OOMOL's Dialpad WFM connector, including schedule and activity or agent metric retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Dialpad WFM through OOMOL-connected credentials, inspect live action schemas, and run schedule or metrics retrieval actions from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-tagged actions may change Dialpad WFM state if run with an unconfirmed payload. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any write-tagged action. <br>
Risk: The current documentation is broader than the listed read-oriented actions. <br>
Mitigation: Fetch the live action schema before constructing payloads and treat any state-changing or destructive behavior as requiring explicit approval. <br>
Risk: Use requires the oo CLI and a connected Dialpad WFM account through OOMOL. <br>
Mitigation: Confirm the user is comfortable using OOMOL's oo CLI and connecting Dialpad WFM before installation or first use. <br>


## Reference(s): <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Dialpad WFM homepage](https://www.dialpad.com/features/workforce-management-software/) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dialpad-wfm) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI JSON responses containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
