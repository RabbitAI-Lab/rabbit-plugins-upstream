## Description: <br>
Generate narrative blog posts from AI coding session transcripts, selecting relevant sessions and producing an agent-narrated account of human-agent collaboration in builder's log, tutorial, or technical deep-dive styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lordshashank](https://clawhub.ai/user/lordshashank) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and technical writers use this skill to turn local AI coding session transcripts into readable development blog posts, with optional publishing support after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read local AI coding transcripts that may contain prompts, code, paths, errors, or secrets. <br>
Mitigation: Select an exact platform, project, time range, or transcript path, and review the generated markdown for sensitive details before sharing. <br>
Risk: The skill can publish derived content online when publishing is enabled. <br>
Mitigation: Confirm the destination and final content before publishing, and provide publishing tokens through environment variables rather than chat. <br>


## Reference(s): <br>
- [Blog Writing Guide](references/blog-writing-guide.md) <br>
- [Devlog Template](assets/devlog-template.md) <br>
- [Claude Code Platform Reference](references/platforms/claude-code/claude-code.md) <br>
- [Codex Platform Reference](references/platforms/codex/codex.md) <br>
- [Gemini CLI Platform Reference](references/platforms/gemini-cli/gemini-cli.md) <br>
- [OpenClaw Platform Reference](references/platforms/openclaw/openclaw.md) <br>
- [OpenCode Platform Reference](references/platforms/opencode/opencode.md) <br>
- [Hashnode Publishing Reference](references/publishing/hashnode/hashnode.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, guidance] <br>
**Output Format:** [Markdown blog post with optional shell commands for session discovery and publishing] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs a local devlog markdown file and reports title, word count, sessions included, time span, and key files referenced.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
