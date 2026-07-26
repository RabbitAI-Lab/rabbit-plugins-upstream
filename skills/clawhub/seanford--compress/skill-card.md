## Description: <br>
Compress natural language memory files such as CLAUDE.md, todos, and preferences into caveman format to save input tokens while preserving technical substance, code, URLs, and structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to reduce token usage in natural language memory files while keeping code blocks, inline code, URLs, file paths, commands, headings, and markdown structure intact. The skill backs up the original file before replacing it with a compressed version. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected markdown or text memory content may be sent to Claude/Anthropic during compression. <br>
Mitigation: Use the skill only on non-sensitive notes and invoke it with an explicit filepath. <br>
Risk: The compressed result replaces the original file. <br>
Mitigation: Keep and review the generated .original.md backup until the compressed output has been checked. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/seanford/skills/compress) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Overwrites the selected natural language file after creating a .original.md backup; validation checks preserved anchors before completion.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
