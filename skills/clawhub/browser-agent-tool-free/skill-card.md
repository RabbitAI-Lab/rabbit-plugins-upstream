## Description: <br>
Guides agents in using a headless browser automation CLI with accessibility-tree snapshots and ref-based element selection for repeatable web navigation, interaction, extraction, screenshots, PDF export, and session state workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent users use this skill to automate browser tasks through CLI commands, including page navigation, deterministic element interaction, content extraction, screenshots, PDF export, and isolated session state handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved browser state files can contain sensitive cookies, storage, or login material. <br>
Mitigation: Keep state JSON files private, out of repositories and logs, and rotate or delete them when no longer needed. <br>
Risk: The workflow depends on a global npm CLI and a Chromium runtime. <br>
Mitigation: Install only in trusted environments, keep the CLI and browser runtime updated, and review generated commands before execution. <br>
Risk: Authenticated browser automation can perform actions with the privileges of the loaded session. <br>
Mitigation: Use separate least-privilege sessions for admin and normal-user testing, and avoid reusing production credentials for exploratory automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/browser-agent-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce browser automation commands and references to local state files; commands require the agent-browser CLI, Node.js, and Chromium runtime.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
