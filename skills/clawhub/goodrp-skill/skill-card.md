## Description: <br>
Detects currently playing Windows media through SMTC and helps an agent query or manage Discord Rich Presence for listening and watching activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[isam-ahmed0](https://clawhub.ai/user/isam-ahmed0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Windows users and agent developers use GoodRP to check what media is currently playing and to show, hide, or override Discord Rich Presence activity. It supports queries about songs or videos, manual presence updates, and auto-show behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose currently playing media, and auto-show can continue displaying future songs or videos on Discord until disabled. <br>
Mitigation: Install only if the external GoodRP application is trusted, enable auto-show intentionally, and use clear_presence or set_auto_show(false) when media should no longer be displayed. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/isam-ahmed0/GoodRP-Skill) <br>
- [GoodRP releases](https://github.com/isam-ahmed0/GoodRP/releases) <br>
- [Bundled GoodRP skill](https://github.com/isam-ahmed0/GoodRP/tree/main/skills/goodrp) <br>
- [Discord Developer Applications](https://discord.com/developers/applications) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON or YAML configuration snippets, and tool-call guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the GoodRP application running on Windows; set_presence requires an explicit watching or listening type.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata; artifact metadata reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
