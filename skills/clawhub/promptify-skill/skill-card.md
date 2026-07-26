## Description: <br>
Promptify Skill optimizes vague or unstructured prompts and can route to clarifying, codebase, or web research helpers when additional context is needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tolibear](https://clawhub.ai/user/tolibear) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, writers, analysts, and other agent users use this skill to turn rough prompts into structured prompts with role, task, constraints, and output requirements. It can ask clarifying questions, inspect relevant project context, or search the web when those steps are requested or auto-detected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Codebase research may inspect relevant project files when +deep is used or auto-detection selects codebase research. <br>
Mitigation: Use it in workspaces where the selected project context is appropriate for agent review, and check generated prompts for sensitive details before sharing them. <br>
Risk: Web research may introduce external guidance that is stale, conflicting, or not applicable to the user's environment. <br>
Mitigation: Review web-informed prompt details against official documentation and current project constraints before relying on them. <br>
Risk: The generated pbcopy command can overwrite clipboard contents or copy sensitive prompt material. <br>
Mitigation: Inspect the command and prompt text before running it, and avoid copying secrets or private data. <br>


## Reference(s): <br>
- [Promptify Skill on ClawHub](https://clawhub.ai/tolibear/skills/promptify-skill) <br>
- [README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with a fenced optimized prompt, an inline clipboard command, and a short explanation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a pbcopy clipboard command; review generated prompt content and commands before use.] <br>

## Skill Version(s): <br>
3.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
