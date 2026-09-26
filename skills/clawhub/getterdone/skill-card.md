## Description:

GetterDone lets an agent hire human gig workers for paid physical or remote tasks, collect proof of work, and route task approval or dispute decisions through user-confirmed workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs help from a human worker for real-world verification, errands, delivery, photography, or human-quality remote work such as writing, design, translation, proofreading, research, or video work. It is also used to manage setup, task posting, worker proof review, payment approval, disputes, event polling, and webhook handling for GetterDone tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid task actions can spend real money or release secured funds.

Mitigation: Keep in-conversation confirmation enabled for task creation, approval, and dispute actions unless the owner has deliberately opted into autonomous review, and use conservative server-side spending caps.

Risk: The GetterDone agent key may persist in an environment variable or credentials file.

Mitigation: Protect the key as a credential, store only the scoped GetterDone key, and revoke it from the dashboard if the machine or credential file may be exposed.

Risk: Task details, locations, attachments, and proof may be shared with GetterDone and assigned workers.

Mitigation: Share only task information required for completion, review attachments before upload, and avoid including secrets, payment details, or unnecessary personal information.

Risk: Autonomous proof review can approve or dispute work without human judgment.

Mitigation: Use autonomous review only as an explicit opt-in path with strict review criteria, wait for media checks where applicable, and fall back to manual review when criteria are absent or ambiguous.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone Platform](https://getterdone.ai)
- [GetterDone Agent Registration](https://getterdone.ai/register-agent)
- [GetterDone API Documentation](https://getterdone.ai/docs/api)
- [GetterDone OpenAPI Specification](https://getterdone.ai/api/openapi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline shell, JSON, REST, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead to paid GetterDone task actions only after the required confirmation or explicit autonomous-review opt-in.]

## Skill Version(s):

1.37.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
