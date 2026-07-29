## Description: <br>
网文去AI味。检测并清除文本中的AI写作痕迹，让文字回归自然、非模板化。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and developers use this skill to detect AI-flavored patterns in Chinese web-fiction drafts and revise prose toward more natural pacing, dialogue, and narrative texture while preserving plot intent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Punctuation normalization can rewrite the specified file when run outside check mode. <br>
Mitigation: Run detection or check-only commands first and keep normal version control or backups before applying cleanup. <br>
Risk: Style cleanup can remove useful narrative detail if applied too broadly. <br>
Mitigation: Review suggested edits against the original plot, character intent, and continuity before accepting changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-deslop) <br>
- [OpenClaw Source Metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [anti-ai-writing.md](references/anti-ai-writing.md) <br>
- [banned-words.md](references/banned-words.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports, rewritten prose, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include detection-only reports, targeted prose edits, review notes, and local script commands.] <br>

## Skill Version(s): <br>
1.1.12 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
