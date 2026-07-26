## Description: <br>
A cat clone with syntax highlighting, line numbers, and Git integration - a modern replacement for cat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to install and apply bat for readable file previews, syntax-highlighted views, line ranges, Git-aware diffs, and pager or configuration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may print the contents of any file the agent is asked to preview. <br>
Mitigation: Review requested paths before use and avoid previewing sensitive files unless disclosure is intended. <br>
Risk: Optional aliases or pager environment settings can change shell behavior until removed. <br>
Mitigation: Prefer session-scoped aliases and document or remove persistent shell configuration changes. <br>


## Reference(s): <br>
- [Bat project documentation](https://github.com/sharkdp/bat) <br>
- [Bat customization documentation](https://github.com/sharkdp/bat#customization) <br>
- [ClawHub skill page](https://clawhub.ai/arnarsson/skills/bat-cat) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash code blocks and short command explanations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the bat executable; install evidence includes Homebrew formula bat and apt package bat.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
