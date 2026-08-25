## Description:

Turn user-supplied risk-grade definitions into a four-to-eight still risk grade set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to create a consistent pack of risk-grade still images from already approved grade names and definitions. The skill plans the pack, confirms billable Beatra image generation, submits one still per grade, and reports returned task and billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra authorization, including spending capability and media/tool scopes.

Mitigation: Install only after reviewing the Beatra publisher and the requested access; require explicit user approval before each billable generation.

Risk: The package stores a shared Beatra Device Token under ~/.beatra for local use.

Mitigation: Keep the token out of prompts, command arguments, logs, and copied files; use the bundled disconnect flow when access should be revoked.

Risk: The bundled client silently checks for and installs verified package updates by default.

Mitigation: Disable automatic updates with scripts/mcp_client.py update --auto off when explicit control over local code changes is required.

Risk: Billable image-generation tasks can create duplicate charges if uncertain submissions are retried with changed inputs.

Mitigation: Use one client_request_id per frozen request, poll or recover existing tasks before retrying, and create a new request ID only for user-approved changed work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/risk-grade-set)
- [Beatra package homepage](https://beatra.ai/skills/risk-grade-set)
- [Risk-grade pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; generated still image artifacts are delivered separately.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One generated still per named risk grade, normally four to eight stills and capped at eight; each still uses a separate approved billable request.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
