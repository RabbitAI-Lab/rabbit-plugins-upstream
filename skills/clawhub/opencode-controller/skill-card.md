## Description: <br>
Control and operate Opencode via slash commands. Use this skill to manage sessions, select models, switch agents (plan/build), and coordinate coding through Opencode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[karatla](https://clawhub.ai/user/karatla) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and coding agents use this skill to operate Opencode sessions through an explicit Plan to Build workflow, including provider selection, authentication confirmation, session reuse, model selection, and handling Opencode questions safely. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to operate Opencode on the user's behalf. <br>
Mitigation: Use a trusted Opencode installation and require explicit user confirmation before provider, authentication, session, and build actions. <br>
Risk: Provider login links could be sensitive or misleading if copied from an untrusted Opencode session. <br>
Mitigation: Verify login links before opening them and wait for user confirmation before continuing authentication. <br>
Risk: Implemented code changes may not match the user's intent if the plan is unclear or incomplete. <br>
Mitigation: Review and approve the plan before switching to Build mode, and return to Plan mode when questions or contradictions appear. <br>


## Reference(s): <br>
- [Command Cheatsheet](references/command-cheatsheet.md) <br>
- [Failure Handling](references/failure-handling.md) <br>
- [Model Selection](references/model-selection.md) <br>
- [Plan vs Build](references/plan-vs-build.md) <br>
- [Question Handling](references/question-handling.md) <br>
- [Session Management](references/session-management.md) <br>
- [Workflow](references/workflow.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/karatla/skills/opencode-controller) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown text with explicit Opencode slash commands and user-facing prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes provider and authentication choices, selected Opencode options, and login links when Opencode provides them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
