## Description: <br>
Story Setup deploys web-novel writing project infrastructure for Claude Code, OpenCode, Codex, ZCode, OpenClaw, Reasonix, and generic agent workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and developers use this skill to set up a dedicated fiction-writing workspace with agents, hooks, rules, commands, and reference material while preserving user-owned project files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs persistent project automation through hooks and configuration changes. <br>
Mitigation: Install it only in a dedicated writing project and review generated hooks and config changes before using the workspace. <br>
Risk: Browser automation may operate with a logged-in browser profile. <br>
Mitigation: Use a separate Chrome profile for browser automation and avoid sharing sensitive browsing sessions with the writing project. <br>
Risk: Network egress may occur through the update check. <br>
Mitigation: Disable the update check when network egress is not wanted. <br>
Risk: The submitted artifact appears to be missing several source templates it references. <br>
Mitigation: Deploy only the CLI targets needed and verify the installation output before trusting generated setup files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-setup) <br>
- [OpenClaw Metadata Source URL](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Upgrade Guide](artifact/UPGRADING.md) <br>
- [Agent Writing References](artifact/references/agent-references/) <br>
- [Codex Hook Merge Helper](artifact/scripts/merge-codex-hooks.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus generated project files, shell commands, JSON/TOML configuration, hooks, and agent definitions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install persistent project automation and CLI-specific hooks depending on the selected target.] <br>

## Skill Version(s): <br>
1.1.15 (source: ClawHub release metadata; artifact frontmatter reports 1.2.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
