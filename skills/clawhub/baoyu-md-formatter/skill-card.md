## Description: <br>
Formats plain text and Markdown by adding or normalizing frontmatter, titles, summaries, headings, bold text, and lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and agent users use this skill to format plain text or Markdown files and produce structured Markdown-oriented outputs. File changes, command execution, and credential use should be reviewed before running in sensitive workspaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ClawHub security evidence marks the release suspicious because it asks for file read/write and command execution authority while documenting unrelated API, credential, and code-development workflows. <br>
Mitigation: Review carefully before installing, run only in a sandboxed workspace, and grant file or command permissions only for the specific formatting task. <br>
Risk: The artifact includes API key setup guidance without identifying a concrete external service or need. <br>
Mitigation: Do not provide API keys or credentials unless the exact service, purpose, and handling requirements are confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/baoyu-md-formatter) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, text, JSON-like status objects, and command or configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write files or propose command execution depending on the agent workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.117.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
