## Description: <br>
Manage TickTick tasks by adding, listing, and completing tasks through the local tickrs CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidsmorais](https://clawhub.ai/user/davidsmorais) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage TickTick tasks on Linux through an authenticated local tickrs CLI, including listing projects and creating, listing, or completing tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates through an authenticated TickTick account and can create or complete tasks. <br>
Mitigation: Review task creation and completion requests before allowing the agent to run them. <br>
Risk: The skill depends on a local tickrs binary and TickTick API credentials. <br>
Mitigation: Install it only where the tickrs binary is trusted, and treat the client secret and CLI session as credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davidsmorais/skills/ticktick-linux) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tool definitions with bash command templates that return JSON from tickrs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the tickrs CLI plus TICKTICK_CLIENT_ID and TICKTICK_CLIENT_SECRET environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
