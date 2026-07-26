## Description: <br>
Verify the bead daemon is alive and responsive <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators who use the beads system use this skill to check whether the local bead daemon is running and accepting commands before relying on bead workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on local bd and ping-beads commands that it does not install or verify. <br>
Mitigation: Confirm those commands resolve to the trusted beads system before running the suggested checks. <br>


## Reference(s): <br>
- [Ping Beads on ClawHub](https://clawhub.ai/xejrax/skills/ping-beads) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires trusted local bd and ping-beads commands; the skill does not install or verify those binaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
