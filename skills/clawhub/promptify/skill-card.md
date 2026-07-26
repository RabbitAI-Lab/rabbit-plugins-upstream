## Description: <br>
Optimize prompts for clarity and effectiveness. Use when user says "improve this prompt", "optimize my prompt", "make this clearer", or provides vague/unstructured prompts. Intelligently routes to sub-agents for codebase research, clarifying questions, or web search as needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tolibear](https://clawhub.ai/user/tolibear) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, writers, analysts, and other agent users use Promptify to turn vague or underspecified requests into structured prompts with clear role, task, constraints, and output expectations. The skill can ask clarifying questions, inspect relevant codebase context, or search current external guidance when the prompt calls for it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Codebase exploration may process private project files or sensitive context when +deep is used or auto-detected. <br>
Mitigation: Avoid +deep and avoid broad project prompts when the workspace contains secrets or private material that should not be processed. <br>
Risk: Web research may send prompt details or context to external search and documentation sources. <br>
Mitigation: Avoid +web and omit confidential details when current external guidance is not required. <br>
Risk: Clipboard output may expose generated prompts to local clipboard history or other applications. <br>
Mitigation: Review the generated clipboard command before running it and skip clipboard copying in sensitive environments. <br>


## Reference(s): <br>
- [Promptify README](README.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/tolibear/skills/promptify) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with an optimized prompt code block, a clipboard shell command, and a short explanation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask clarifying questions or gather codebase and web context before producing the optimized prompt.] <br>

## Skill Version(s): <br>
3.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
