## Description:

AI Video Restyler helps agents restyle one short source video into a coherent new visual treatment while preserving the source subject, action, composition, and camera intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and production agents use this skill to turn a short source clip into an anime, illustration, Chinese comic, ink, clay, paper-cut, cyberpunk, retro-film, or reference-led visual treatment while preserving core motion and composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared broad Beatra device token stored in local user state.

Mitigation: Authorize only through the bundled helper, keep the credential file private, and revoke or uninstall through the documented Beatra flows when access is no longer needed.

Risk: Source videos and optional references are sent to Beatra for remote video processing.

Mitigation: Use only media the user is comfortable submitting, inspect local files before upload, and pass returned artifact references rather than local paths to remote tools.

Risk: The bundled client enables silent package self-updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when explicit review of package changes is required.

Risk: Paid video restyling can create duplicate charges if a request is resubmitted with changed arguments or a new request identity after uncertainty.

Mitigation: Show a prepaid admission card, wait for explicit balance confirmation, freeze one `client_request_id`, submit exactly once, and recover uncertain responses using the identical payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-video-restyler)
- [Beatra skill homepage](https://beatra.ai/skills/ai-video-restyler)
- [Video restyle workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples; final task reporting may include returned video artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports only returned task status, usage, billing, and inspectable output review; avoids exposing credentials or private prompts.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
