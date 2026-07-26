## Description: <br>
Kernel operates Kernel browser sessions through the OOMOL `kernel` connector and `oo` CLI for reading, creating, updating, and deleting session data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Kernel browser sessions from an agent through an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Kernel browser sessions through an OOMOL-connected account. <br>
Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before deleting a named or identified session. <br>
Risk: The skill uses server-side OOMOL credential injection to act on the connected account. <br>
Mitigation: Install it only when the agent is intended to manage Kernel sessions, and review prompts carefully before approving create, update, or delete actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kernel) <br>
- [Kernel Homepage](https://kernel.sh) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with `oo` CLI shell commands and JSON connector payloads or responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence metadata and release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
