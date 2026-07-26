## Description: <br>
Stormboard lets an agent search and read Stormboard data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Stormboard users use this skill to let an agent inspect Stormboard profile, board, access, idea, user, tag, connector, and template data from a connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Stormboard data available to the user's connected OOMOL/Stormboard account. <br>
Mitigation: Install only when agent access to that Stormboard data is intended, and keep use to the documented get and list actions. <br>
Risk: First-time setup may ask the user to install or sign in to the oo CLI when a command fails. <br>
Mitigation: Review any requested installation or login step before allowing it, and do not run connection steps unless the matching error occurs. <br>
Risk: Future connector actions could claim to change or delete Stormboard data. <br>
Mitigation: Require explicit user confirmation before any action that writes, overwrites, or deletes Stormboard data. <br>


## Reference(s): <br>
- [ClawHub Stormboard Skill](https://clawhub.ai/oomol/skills/oo-stormboard) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Stormboard](https://stormboard.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-oriented get/list actions; requires an installed, signed-in oo CLI and a connected Stormboard account.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
