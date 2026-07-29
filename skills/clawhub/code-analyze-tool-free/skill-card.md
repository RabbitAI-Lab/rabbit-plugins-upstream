## Description: <br>
代码分析工具免费版 helps personal developers turn code, data, text, decisions, and visualization inputs into prioritized, source-labeled Markdown analysis with counter-evidence and action recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to structure personal code review, technical option selection, data report analysis, and other decision-oriented analysis tasks. It guides the agent to choose an analysis framework, label priorities and sources, challenge conclusions, and return actionable Markdown output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags broad read/search plus possible shell and write access for a Markdown-driven analysis workflow. <br>
Mitigation: Review the skill before installation, grant it only in workspaces where local file access and command execution are acceptable, and inspect proposed commands or file writes before allowing them. <br>
Risk: The security review notes callback and network references despite local-only claims. <br>
Mitigation: Avoid using callback_url or network-related steps unless the expected data flow is clarified and acceptable for the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-analyze-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with text examples, shell snippets, and optional JSON configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs emphasize priority labels, source labels, counter-evidence, and action recommendations. The artifact recommends keeping single inputs under 50000 characters.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
