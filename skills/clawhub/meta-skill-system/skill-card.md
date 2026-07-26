## Description: <br>
A Chinese-language meta-skill for domain evaluation, workflow restructuring, skill generation, and general task execution using catalog, requirements, and exemplar reference files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide agents through methodology tasks such as evaluating whether a domain should exist, simplifying workflows for AI-assisted execution, generating new skill artifacts, and producing structured analysis or plans. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has a broad activation scope and can guide agents through skill generation, workflow restructuring, web research, file operations, and possible shell or Python use. <br>
Mitigation: Use explicit task boundaries and require confirmation before running commands, writing files, editing generated skills, or relying on external search results. <br>
Risk: Security evidence marks the release as suspicious because the shell and Python fallback is under-scoped. <br>
Mitigation: Review the requested action before installation or execution, and prefer sandboxed execution with user approval for file and command operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/meta-skill-system) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/wangjiaocheng) <br>
- [Meta-skill catalog](references/meta-skill-catalog.md) <br>
- [Meta-skill requirements](references/meta-skill-requirements.md) <br>
- [Exemplars index](references/exemplars.md) <br>
- [Full prompt bundle](references/meta-skill-system-prompt.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce structured plans, generated skill files, search guidance, command suggestions, and review checklists depending on the user task.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
