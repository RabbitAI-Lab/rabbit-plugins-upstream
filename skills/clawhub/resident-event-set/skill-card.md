## Description:

Turn user-supplied resident event names and points into a four-to-eight still resident event set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative operators use this skill to plan and generate a coordinated pack of resident event stills from event names and points they already have. It helps keep each activity still aligned to the confirmed pack list, shared visual style, billing approval, and task recovery process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary reports broad Beatra account capabilities and a shared local bearer token.

Mitigation: Review the requested Beatra authorization before installation, keep credentials out of chat and logs, and disconnect the skill if the account scopes are not acceptable.

Risk: The server security summary reports silent package self-updates by default.

Mitigation: Disable automatic updates with the documented update control command when the environment requires explicit approval before code changes.

Risk: The skill can spend Beatra credits through image-generation requests.

Mitigation: Require the documented production card and user approval before each billable generation, use one client_request_id per still, and do not resubmit uncertain paid work with changed arguments.

Risk: The skill may upload local reference files when the user supplies visual references.

Mitigation: Upload only user-approved reference files, preserve exact MIME details, and avoid exposing private prompts, tokens, or sensitive input content during recovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/resident-event-set)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Resident event pack workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra skill homepage](https://beatra.ai/skills/resident-event-set)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and generated image artifact delivery details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans and submits one paid image-generation task per confirmed activity still; reports returned task IDs, resolved models, dimensions, formats, and billing.net_charged_credits when available.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
