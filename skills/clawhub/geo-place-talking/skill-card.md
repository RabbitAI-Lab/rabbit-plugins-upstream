## Description:

Turn a user-supplied geography place table and authorized stills into one geography place talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and agents supporting classroom geography content use this skill to turn a supplied place table and authorized stills into short talking geography clips. It plans one slot per still, prepares speech or approved audio, and requests Beatra video animation only after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared broad Beatra account credential and a generic remote tool caller.

Mitigation: Install only if the Beatra approval scopes are acceptable, keep the credential private, and provide only media and place-table content the user is authorized to upload or clone.

Risk: The bundled client performs silent package update checks and can automatically install newer verified releases by default.

Mitigation: Review the update behavior before use and disable automatic updates for the installation with `python3 scripts/mcp_client.py update --auto off` when change control is required.

Risk: The workflow can trigger paid clone, speech, and video generation tasks.

Mitigation: Use the staged approval cards, live model and price checks, opaque request IDs, and task polling guidance before submitting billable work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/geo-place-talking)
- [Beatra skill homepage](https://beatra.ai/skills/geo-place-talking)
- [Geography place talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free slot list first; paid clone, speech, and video stages require separate confirmation and task polling.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
