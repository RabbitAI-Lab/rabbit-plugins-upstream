## Description:

Integrate Dida365 safely through Pontx. Use for credential setup, task or project reads and writes, scheduling, recurrence, completion, moves, or any Dida365 Open API workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external integration builders use this skill to inspect current Pontx Dida365 API and SDK facts, implement read or write workflows, and manage task, project, scheduling, recurrence, completion, and move operations with explicit previews before mutation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or access tokens could be exposed through source, command arguments, logs, or chat.

Mitigation: Keep secrets in environment variables or a secret manager, isolate hosted user credentials server-side, and revoke or replace exposed tokens before continuing.

Risk: Task writes, moves, completions, or deletions can change real Dida365 data if the target or schedule is wrong.

Mitigation: Preview every non-read action with the resolved account, project, task identifiers, schedule, body, and expected effect, then require explicit approval for that exact preview.

Risk: Ambiguous retries or incomplete state checks can duplicate creates or repeat destructive effects.

Mitigation: Read relevant state before ambiguous creates, completions, moves, or deletions, and avoid blindly retrying mutations.

Risk: Dida365 account content can include personal data.

Mitigation: Narrow reads by project or time range where supported and return only the information needed for the user's task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-dida365)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and code guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill emphasizes current API inspection, credential safety, scoped reads, previewed non-read actions, and explicit approval before mutations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
