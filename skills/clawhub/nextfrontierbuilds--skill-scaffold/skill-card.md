## Description: <br>
AI agent skill scaffolding CLI. Create skills for OpenClaw, Moltbot, Claude, Cursor, ChatGPT, Copilot instantly. Vibe-coding ready. MCP compatible. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use Skill Scaffold to generate local skill templates for ClawHub/OpenClaw-style skills, MCP servers, and generic agent skill structures. It produces editable SKILL.md, README.md, optional scripts, and optional CLI boilerplate so teams can start a new skill package quickly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated templates may contain placeholder descriptions, authors, trigger text, and implementation TODOs that are unsuitable for direct publication. <br>
Mitigation: Review generated SKILL.md, README.md, and optional CLI files before publishing them or letting another agent rely on them. <br>
Risk: The CLI writes files into a user-selected target directory, so accidental output paths can create files somewhere unintended. <br>
Mitigation: Run it from the intended workspace or pass an explicit output directory, then inspect the generated files before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextfrontierbuilds/skills/skill-scaffold) <br>
- [npm package](https://www.npmjs.com/package/skill-scaffold) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Generated local files containing Markdown, JavaScript, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a new skill directory; optional flags select template, output directory, author, description, scripts, and CLI scaffold.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter, package.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
