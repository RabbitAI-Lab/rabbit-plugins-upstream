## Description: <br>
Use this skill for Mailjet requests involving reading, creating, and updating contact data through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Mailjet contacts through an OOMOL-connected account, including listing, retrieving, creating, and updating contacts. It is intended for agent workflows that need schema-checked Mailjet operations without handling raw Mailjet credentials directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed write actions can create or update Mailjet contacts. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running create_contact or update_contact. <br>
Risk: Mailjet access is mediated through OOMOL and depends on the user's connected account. <br>
Mitigation: Install or reconnect the oo CLI only when commands fail for missing CLI, authentication, connection, scope, credential, app, or billing reasons. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailjet) <br>
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Mailjet homepage](https://www.mailjet.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing payloads and to obtain confirmation before write actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
