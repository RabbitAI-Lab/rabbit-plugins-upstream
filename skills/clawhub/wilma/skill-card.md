## Description:

Helps AI agents retrieve schedules, homework, grades, lesson notes, messages, news, and school documents from Finland's Wilma system through WilmAI tools or its CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aikarjal](https://clawhub.ai/user/aikarjal)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and guardians use an AI agent to review their children's school updates, follow up on messages, and retrieve relevant documents from Wilma.

### Deployment Geography for Use:

Finland

## Known Risks and Mitigations:

Risk: Wilma access exposes sensitive student records and messages.

Mitigation: Limit access to the user's authorized account and share only the school information needed for the request.

Risk: Login credentials and saved sessions can be exposed if handled in chat or left on a shared computer.

Mitigation: Use browser login or secret/environment settings instead of pasting passwords into chat; remove saved logins when no longer needed.

Risk: Downloaded school documents may persist outside the intended task.

Mitigation: Save downloads in a task-specific folder and remove them when no longer needed.

Risk: CLI installation or fallback may fetch a third-party package.

Mitigation: Install only if the user trusts the WilmAI CLI package and needs Wilma access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/aikarjal/skills/wilma)
- [WilmAI website](https://wilm.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summaries and downloaded school documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents can be saved to a task-specific folder on request.]

## Skill Version(s):

2.1.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
