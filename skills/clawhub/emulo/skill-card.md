## Description: <br>
Load the user's Emulo profile, mined from their local Claude Code, Codex, and OpenCode session logs, so you work like them instead of a cold start. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ohad6k](https://clawhub.ai/user/ohad6k) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Emulo before coding or writing tasks to load a local working profile that captures the user's preferences, voice, and recurring failure modes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive local profile material derived from the user's AI coding history. <br>
Mitigation: Install only when the user wants agents to use that local profile, and review the generated profile before relying on it. <br>
Risk: Persisting the profile into agent instruction files can affect future agent behavior. <br>
Mitigation: Prefer the MCP loader when only loading an existing profile, and review any persisted instruction-file changes before use. <br>


## Reference(s): <br>
- [ClawHub Emulo Skill](https://clawhub.ai/ohad6k/skills/emulo) <br>
- [Emulo Project Homepage](https://github.com/ohad6k/emulo) <br>
- [Emulo v0.5.0 Release Notes](https://github.com/ohad6k/emulo/releases/tag/v0.5.0) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown profile text with shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May load an existing profile through MCP or persist profile guidance into agent instruction files when requested.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
