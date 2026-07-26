## Description: <br>
Provide new contributors and agents with a concise tour of the workspace identity files (SOUL.md, USER.md, AGENTS.md, TOOLS.md) plus onboarding tips. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, agents, and workspace contributors use this skill to quickly orient themselves to local identity, user guidance, agent rules, tooling notes, and onboarding expectations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local files selected through --workspace and --files, which could expose sensitive content if pointed at secrets, private configuration, or unrelated system paths. <br>
Mitigation: Run it only against trusted project documentation and avoid including secrets, SSH keys, tokens, private configs, or unrelated system paths. <br>


## Reference(s): <br>
- [Context Onboarding Guidelines](references/context-guidelines.md) <br>
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/context-onboarding) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text summaries with Markdown-oriented guidance and example shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Summaries are based on user-selected local workspace files and the requested line count or brief mode.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
