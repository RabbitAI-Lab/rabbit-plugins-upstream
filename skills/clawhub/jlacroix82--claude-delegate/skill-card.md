## Description: <br>
Delegate coding, repository analysis, file edits, test runs, or code review to the local Claude Code CLI without embedding an Anthropic API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to delegate repository analysis, code review, debugging, test investigation, and file-editing tasks to a locally authenticated Claude Code CLI from a trusted workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The delegated Claude Code run can read repository content and, when write permissions are enabled, modify workspace files. <br>
Mitigation: Start with read-only mode, use workspace-write only for intended edits, and inspect relevant diffs before reporting changes. <br>
Risk: The danger-full-access mode grants unrestricted local access. <br>
Mitigation: Reserve danger-full-access for isolated environments with explicit operator approval. <br>
Risk: Optional JSON logging can store sensitive prompts, repository snippets, tool output, and responses on disk. <br>
Mitigation: Avoid --json-log unless local storage of that information is acceptable for the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/claude-delegate) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text or Markdown final responses from Claude Code, with optional JSON or stream-json logs when configured.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or edit workspace files when write permissions are selected; optional local logs can store prompts, repository snippets, tool output, and responses.] <br>

## Skill Version(s): <br>
0.1.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
