## Description: <br>
Operates LangSmith through an OOMOL-connected account for reading, creating, and updating workspace, project, dataset, example, and tracing data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate LangSmith workspaces, projects, datasets, examples, and tracing resources through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create LangSmith projects, datasets, and examples. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions marked as write. <br>
Risk: The skill depends on an OOMOL-connected LangSmith account and valid credentials. <br>
Mitigation: Use a least-privilege LangSmith token and only run first-time setup steps after an authentication or connection failure. <br>
Risk: Broad trigger wording may cause the skill to be selected for many LangSmith-related requests. <br>
Mitigation: Inspect the live action schema before execution and avoid write operations unless the user explicitly confirms them. <br>


## Reference(s): <br>
- [LangSmith skill on ClawHub](https://clawhub.ai/oomol/skills/oo-langsmith) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [LangSmith homepage](https://www.langchain.com/langsmith) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
