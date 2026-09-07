## Description:

Turns authorized host or room stills and confirmed stay facts into ordered 2-15 second Beatra welcome or amenity talking clips, one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External hosts and property managers use this skill to plan and generate short Beatra speech-and-video clips for check-in greetings, amenity explainers, and guest arrival messages from authorized stills and confirmed stay facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra account credential with broad generation, task, artifact, and spending-related privileges.

Mitigation: Review the Beatra approval page before authorizing, protect `~/.beatra/credentials.json`, and revoke the connected agent when the skill is no longer needed.

Risk: Silent package updates are enabled by default, which can change package code after installation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when change control is required, and use explicit update checks instead.

Risk: Paid speech and video generation can consume credits, and retrying changed requests can create duplicate work.

Mitigation: Use a separate production card for each paid stage, keep one opaque `client_request_id` per frozen payload, and retry only identical requests after transport uncertainty.

Risk: Welcome clips can misstate stay facts or misuse likeness or voice rights if inputs are not confirmed.

Mitigation: Use only host-confirmed facts, require likeness and voice rights before face or cloned-voice use, and review the generated clips against the original stills and spoken facts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/airbnb-welcome-avatar)
- [Beatra package homepage](https://beatra.ai/skills/airbnb-welcome-avatar)
- [Homestay welcome talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON payloads and inline shell commands; generated media is returned as Beatra task artifacts with usage and billing summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one ordered welcome or amenity clip per authorized still; paid speech and video generation stages require separate confirmation.]

## Skill Version(s):

0.1.3 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
