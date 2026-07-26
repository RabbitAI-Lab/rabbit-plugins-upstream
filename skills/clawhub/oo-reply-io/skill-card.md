## Description: <br>
Reply.io lets agents operate a user's OOMOL-connected Reply.io account to read, create, and update contacts and manage sequences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent work with Reply.io contacts and sequences through their connected account. It supports reading user, contact, and sequence data plus confirmed write actions such as creating or updating contacts and starting or pausing sequences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update contacts and start or pause Reply.io sequences, changing business outreach data. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write. <br>
Risk: The skill operates through the user's OOMOL-connected Reply.io account. <br>
Mitigation: Install and use it only when the agent should access that Reply.io account, and review action requests before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-reply-io) <br>
- [Reply.io Homepage](https://reply.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
