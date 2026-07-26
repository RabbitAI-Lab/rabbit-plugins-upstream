## Description: <br>
Detects and edits Chinese web-fiction prose to reduce AI-flavored, formulaic writing while preserving plot, character details, and author intent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and editors use Story Deslop to scan Chinese web-fiction drafts for formulaic AI-style prose and receive targeted rewrite guidance, reports, or file edits that make the text read more naturally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File mode can rewrite provided manuscript files and normalize punctuation after editing. <br>
Mitigation: Keep backups and request detection-only behavior when review is needed before any edits are applied. <br>
Risk: Aggressive style cleanup can remove useful plot, character, or pacing detail if applied too broadly. <br>
Mitigation: Review the change report, preserve story intent, and use the skill's review markers for uncertain edits. <br>


## Reference(s): <br>
- [Story Deslop on ClawHub](https://clawhub.ai/worldwonderer/skills/story-deslop) <br>
- [Publisher profile](https://clawhub.ai/user/worldwonderer) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Anti-AI Writing Guide](references/anti-ai-writing.md) <br>
- [Banned Words and Patterns](references/banned-words.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown reports with edited prose, inline shell commands, and optional file edits] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [File mode can update user-supplied manuscript files and return short representative excerpts for long inputs.] <br>

## Skill Version(s): <br>
1.1.11 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
