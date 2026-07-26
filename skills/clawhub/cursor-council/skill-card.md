## Description: <br>
Multi-Cursor orchestration for parallel task execution and AI council deliberation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaoyaner0201](https://clawhub.ai/user/xiaoyaner0201) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to coordinate multiple Cursor agent sessions for independent coding tasks, architecture reviews, technology choices, risk assessments, and synthesis of multi-model technical recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Parallel Cursor agents may edit files or run commands with reduced approval prompts. <br>
Mitigation: Run sessions in separate branches or disposable worktrees, keep task boundaries explicit, and supervise approval prompts instead of accepting them blindly. <br>
Risk: Concurrent sessions can overwrite or conflict with each other's changes. <br>
Mitigation: Assign each session independent files or modules, stage dependent work, monitor sessions with tmux capture, and merge only after review and validation. <br>
Risk: Council prompts and archived outputs may contain sensitive project, customer, or business information. <br>
Mitigation: Avoid including secrets or sensitive data in prompts, store transcripts only where access is controlled, and delete archives when they are no longer needed. <br>


## Reference(s): <br>
- [Cursor Council on ClawHub](https://clawhub.ai/xiaoyaner0201/skills/cursor-council) <br>
- [Council Deliberation Guide](references/council-deliberation.md) <br>
- [Parallel Execution Guide](references/parallel-execution.md) <br>
- [Persona Engineering for AI Council](references/persona-engineering.md) <br>
- [Session README Template](references/session-readme-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces orchestration instructions, task decomposition guidance, prompt templates, and council-session archive templates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
