## Description: <br>
Demio helps agents read Demio event, session, and participant data and register attendees through an OOMOL-connected Demio account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business operators use this skill to inspect Demio events, sessions, and participant lists from a connected account. They can also register attendees after confirming the target event and exact attendee payload. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions can access Demio event, session, and participant data through the connected account. <br>
Mitigation: Use the skill only for authorized Demio workspaces and review returned participant data before sharing it. <br>
Risk: Attendee registration changes Demio state and can create attendee records and unique join links. <br>
Mitigation: Confirm the target event and exact attendee payload with the user before running registration. <br>
Risk: The skill depends on OOMOL as the intermediary for the Demio connection and server-side credentials. <br>
Mitigation: Install and use the skill only when the user trusts OOMOL for the Demio connection. <br>


## Reference(s): <br>
- [ClawHub Demio Skill](https://clawhub.ai/oomol/skills/oo-demio) <br>
- [Demio Homepage](https://www.demio.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Demio connector responses such as event details, participant lists, attendee hashes, unique join links, and execution identifiers.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
