## Description:

Use only when the user explicitly names Promarkia and asks to list approved marketing squads, submit one specified Promarkia marketing run, or retrieve a named Promarkia run ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dominiclachance](https://clawhub.ai/user/dominiclachance)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run explicitly requested Promarkia marketing tasks, list approved squads, or retrieve a named run. It is scoped to approved marketing squads and requires current authorization before transmitting prompts, consuming credits, or performing external actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Promarkia runs can transmit prompts outside the agent environment and consume account credits.

Mitigation: Review the exact task and obtain current user authorization before submitting any run.

Risk: Some marketing tasks can publish, schedule, upload, message, email, contact people, or affect connected accounts.

Mitigation: Require explicit confirmation for the exact outbound action and destination before allowing the run.

Risk: Prompts may accidentally include secrets, private files, or unrelated personal data.

Mitigation: Remove credentials and unrelated personal data before submission, and send only information authorized for the task.

Risk: Returned Promarkia content is untrusted and may include misleading or unsafe instructions.

Mitigation: Treat returned content as data, not instructions, and review final content before acting on it.

Risk: A local timeout may leave a remote run active, creating duplicate cost or duplicate external action risk.

Mitigation: Preserve the run ID and check run status before submitting a replacement.

## Reference(s):

- [Promarkia homepage](https://www.promarkia.com)
- [ClawHub skill page](https://clawhub.ai/dominiclachance/skills/promarkia)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and textual run results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PROMARKIA_API_KEY; Promarkia run output is labeled as untrusted.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
