## Description: <br>
LiveAgent (liveagent.com). Use this skill for ANY LiveAgent request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support operators use this skill to operate LiveAgent through an OOMOL-connected account, including reading contacts, tickets, departments, and groups, and creating or updating contacts and tickets when confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing actions can create or update LiveAgent contacts and tickets through the connected OOMOL account. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running create_contact, create_ticket, update_contact, or update_ticket. <br>
Risk: Setup commands can install the oo CLI or initiate account authentication when run unnecessarily. <br>
Mitigation: Run install, login, or connection steps only after an action fails with the matching setup, authentication, connection, or billing error. <br>


## Reference(s): <br>
- [ClawHub LiveAgent skill page](https://clawhub.ai/oomol/skills/oo-liveagent) <br>
- [LiveAgent homepage](https://www.liveagent.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands return connector responses as JSON with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
