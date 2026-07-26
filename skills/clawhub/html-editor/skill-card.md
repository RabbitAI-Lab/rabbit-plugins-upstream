## Description: <br>
Turns static HTML files into visually editable pages with inline text editing, style controls for colors, fonts and layout, style-prompt copying, and clean HTML export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ytisvibecoding](https://clawhub.ai/user/ytisvibecoding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content teams, and AI-agent users use this skill to convert local or static HTML reports, pages, and presentations into editable HTML with a browser style panel and export workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The normal command reads a local HTML input and writes a modified editable HTML copy with injected editor assets and browser localStorage state. <br>
Mitigation: Run it only on files intended for editable copies, keep the original file, and review the generated HTML before sharing or deploying it. <br>
Risk: If ANTHROPIC_API_KEY or OPENAI_API_KEY is set, optional label generation may send CSS variable metadata and selectors to the configured provider. <br>
Mitigation: Unset those environment variables when offline-only processing is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ytisvibecoding/skills/html-editor) <br>
- [Publisher profile](https://clawhub.ai/user/ytisvibecoding) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance and generated HTML files with injected CSS and JavaScript] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces an editable *-editable.html copy of the input HTML; optional LLM label generation may use Anthropic or OpenAI API keys when present.] <br>

## Skill Version(s): <br>
1.8.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
