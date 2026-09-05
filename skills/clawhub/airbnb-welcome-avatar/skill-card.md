## Description:

Turns authorized host or room stills and confirmed stay facts into one 2-15 second homestay welcome or amenity talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External hosts, property managers, and their agents use this skill to plan and generate short welcome, check-in, and amenity talking clips from authorized property stills and confirmed stay facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a shared Beatra device credential with broad media, task, artifact, and wallet-spend authority.

Mitigation: Install only when that account-level access is acceptable, keep the token only in the local credential file, and revoke or reconnect the device when access is no longer needed.

Risk: Automatic updates are enabled by default and can replace installed package code from Beatra's vetted channel.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required.

Risk: Speech and video generation can spend Beatra credits and can be duplicated if recovery is handled incorrectly after transport uncertainty.

Mitigation: Review each production card before approving a paid call, reuse the same `client_request_id` only for unchanged recovery, and wait for top-up confirmation before retrying insufficient-balance requests.

Risk: Welcome clips can misuse likeness, voice, or property facts if the inputs are not authorized or confirmed.

Mitigation: Use only authorized stills, confirmed stay facts, and confirmed likeness or voice rights; do not invent rules, fees, access details, or amenities.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/airbnb-welcome-avatar)
- [Beatra skill homepage](https://beatra.ai/skills/airbnb-welcome-avatar)
- [Homestay welcome talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown with storyboard text, production cards, command snippets, and final artifact summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one ordered 2-15 second clip per still; paid speech and video stages require separate confirmation.]

## Skill Version(s):

0.1.2 (source: manifest.json and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
