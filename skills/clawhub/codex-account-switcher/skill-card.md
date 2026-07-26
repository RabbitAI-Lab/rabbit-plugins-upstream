## Description: <br>
Manage multiple OpenAI Codex accounts by capturing current login tokens, switching between saved accounts, and auto-selecting the best one based on quota budget scoring, with optional explicit sync of saved Codex tokens into local OpenClaw agent auth stores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Codex CLI users use this skill to save, list, switch, compare, and auto-select local Codex account credentials. It can also explicitly sync saved Codex tokens into selected OpenClaw agent authentication stores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads, writes, and duplicates local Codex access and refresh tokens. <br>
Mitigation: Install only in trusted local environments, keep Codex and OpenClaw auth files private, and restrict filesystem permissions on token files and account snapshots. <br>
Risk: Running commands may save or refresh a local credential snapshot even when the user did not intend to persist token state. <br>
Mitigation: Review saved account snapshots after use and avoid running the tool on shared or untrusted machines. <br>
Risk: OpenClaw sync can copy saved Codex tokens into agent authentication stores. <br>
Mitigation: Use sync --dry-run before writing and use --agent to limit token propagation to specific agents. <br>


## Reference(s): <br>
- [Codex Account Switcher on ClawHub](https://clawhub.ai/odrobnik/skills/codex-account-switcher) <br>
- [Skill README](SKILL.md) <br>
- [Setup Instructions](SETUP.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local JSON authentication file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and the Codex CLI; reads and writes local Codex and OpenClaw authentication files declared in ClawHub metadata.] <br>

## Skill Version(s): <br>
1.4.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
