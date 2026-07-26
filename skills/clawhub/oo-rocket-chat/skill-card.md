## Description: <br>
Rocket.Chat lets an agent read rooms and messages and, with confirmation, post, update, or delete messages through OOMOL's Rocket.Chat connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate a connected Rocket.Chat workspace from Codex, including profile and room lookups, message reads, and confirmed message changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post, update, or delete Rocket.Chat messages when write or destructive actions are requested. <br>
Mitigation: Confirm the exact target, payload, and effect with the user before running post, update, or delete actions. <br>
Risk: First-time setup may install the oo CLI or connect Rocket.Chat credentials through OOMOL. <br>
Mitigation: Run setup steps only after the matching auth, connection, or missing-CLI failure, and install this skill only when OOMOL is trusted for the connected account. <br>


## Reference(s): <br>
- [Rocket.Chat ClawHub skill](https://clawhub.ai/oomol/skills/oo-rocket-chat) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Rocket.Chat homepage](https://www.rocket.chat) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions are expected to return JSON when executed with the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
