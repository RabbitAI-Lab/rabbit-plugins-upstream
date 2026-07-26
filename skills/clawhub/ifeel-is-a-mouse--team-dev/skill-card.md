## Description: <br>
Multi-agent team development. Triggered by team-dev or team development. Orchestrates 6 specialist agents for spec-to-delivery with quality gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ifeel-is-a-mouse](https://clawhub.ai/user/ifeel-is-a-mouse) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate multi-agent software delivery from requirements through design, implementation, testing, audit, and release documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent agent identities and shared workspace links under ~/.openclaw. <br>
Mitigation: Review the AGENTS.md and SOUL.md templates before initialization and prefer a disposable or project-scoped workspace for first use. <br>
Risk: Some workflow instructions are under-scoped or contradictory, including local-only Git guidance alongside a coder push checklist. <br>
Mitigation: Clarify whether remote Git operations are allowed before running delivery stages, and remove or constrain push steps when operating in local-only mode. <br>
Risk: Custom regions in agent identity files are preserved across updates, which can retain prior behavior. <br>
Mitigation: Inspect preserved custom content during initialization or upgrade and confirm it is appropriate for the current workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ifeel-is-a-mouse/skills/team-dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions, generated project files, shell commands, code changes, and review reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command-only invocation; may create persistent agent identity files, shared workspace links, and project delivery artifacts.] <br>

## Skill Version(s): <br>
4.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
