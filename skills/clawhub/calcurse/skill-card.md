## Description: <br>
A text-based calendar and scheduling application. Use strictly for CLI-based calendar management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent query and update a local calcurse calendar from the command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar queries may expose personal schedule details to the agent. <br>
Mitigation: Use the skill only when the agent is allowed to inspect local calendar data. <br>
Risk: Calendar update commands can create local appointments or todos. <br>
Mitigation: Review dates, times, durations, descriptions, and priorities before allowing updates. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local calcurse binary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
