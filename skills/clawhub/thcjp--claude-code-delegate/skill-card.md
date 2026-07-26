## Description: <br>
Delegates coding tasks to a local AI coding CLI with non-interactive execution, asynchronous polling, session continuation, independent test verification, environment checks, safety guidance, and result relay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to delegate code writing, modification, review, testing, and debugging tasks to an external local coding CLI while preserving asynchronous user interaction and requiring independent verification of generated code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run an external AI coding CLI with broad file-write authority. <br>
Mitigation: Use only disposable or tightly isolated project directories and avoid repositories containing secrets or account configuration. <br>
Risk: Write protection is recommended but optional in the artifact behavior. <br>
Mitigation: Enable a real write guard or sandbox before delegation and review warnings when protection is missing. <br>
Risk: Automatic delegation can execute coding actions for routine edits. <br>
Mitigation: Prefer explicit delegation triggers for ordinary edits and review delegated outputs before applying or relaying results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-code-delegate) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include delegated task summaries, changed-file summaries, test results, CLI status polling guidance, and safety warnings.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 0.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
