## Description: <br>
Devin lets an agent operate Devin organization sessions through an OOMOL-connected account, including creating, listing, inspecting, messaging, and terminating sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to manage Devin organization sessions from an agent workflow while relying on live connector schemas before each action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create sessions, send messages, and terminate Devin sessions through a connected account. <br>
Mitigation: Review prompts carefully and confirm exact payloads before approving write or destructive actions. <br>
Risk: First-time setup may require installing the oo CLI through a remote installer command. <br>
Mitigation: Treat the one-time CLI installation command like any remote installer and review it before execution. <br>
Risk: A missing, expired, or under-scoped Devin connection can block actions. <br>
Mitigation: Use the documented setup and connection recovery steps only after an auth, connection, scope, or billing failure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-devin) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Devin homepage](https://devin.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action calls; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
