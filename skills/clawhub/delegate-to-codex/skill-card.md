## Description:

Guides an orchestrator in handing explicitly requested repository work to Codex CLI, from model selection and execution through review of returned changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[troioi-vn](https://clawhub.ai/user/troioi-vn)

### License/Terms of Use:

MIT

## Use Case:

Developers and other orchestrators use this skill when a user explicitly asks to delegate repository work to Codex CLI. It helps prepare and run the handoff, review the returned changes, and validate the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and could not resolve several path-like references, so its benign verdict does not establish that every referenced resource was reviewed.

Mitigation: Review referenced resources before relying on the scan verdict.

Risk: A delegated run may continue after the current session ends, and the selected model may use the user's quota or incur costs.

Mitigation: Check the model, costs, and quota before execution, and decide whether background jobs should continue after the session.

Risk: The handoff and repository content read by Codex are sent to the configured model provider.

Mitigation: Do not delegate repositories or include secrets that the user would not share with that provider.

## Reference(s):

- [Codex CLI documentation](https://developers.openai.com/codex/cli)
- [Codex Skill release on ClawHub](https://clawhub.ai/troioi-vn/skills/delegate-to-codex)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown instructions with handoff prompt and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific handoff guidance, execution steps, and review checklists]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
