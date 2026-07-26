## Description: <br>
Discord Bot lets an agent read, create, update, and delete Discord Bot data through OOMOL's discordbot connector and oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent manage Discord Bot workflows, including reading Discord resources and performing confirmed write or destructive operations through OOMOL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some state-changing Discord actions may be untagged even though the skill treats untagged actions as safe to run directly. <br>
Mitigation: Require explicit user confirmation for any action that posts, pins, crossposts, unbans, prunes members, changes roles or channels, or deletes data. <br>
Risk: The skill can operate a connected Discord Bot through OOMOL and may affect guilds, channels, messages, roles, members, threads, invites, stickers, emojis, and application commands. <br>
Mitigation: Review the bot's Discord permissions and OOMOL connection before installation and before running sensitive actions. <br>


## Reference(s): <br>
- [ClawHub Discord Bot skill page](https://clawhub.ai/oomol/skills/oo-discordbot) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Discord Developer Applications](https://discord.com/developers/applications) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when commands are run.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
