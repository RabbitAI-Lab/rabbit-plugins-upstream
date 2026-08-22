## Description:

Make a pet talk by animating one clear pet photo with a short message or prepared voice clip, then review breed and face identity, mouth motion, speech clarity, and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and pet owners use this skill to turn one clear pet photo plus approved speech into a shareable talking-pet video for greetings, jokes, reactions, stories, festive messages, or pet-creator content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists a shared local Beatra Device Token with broad media and spending-related authority.

Mitigation: Install only if that shared authorization is acceptable, keep the token local, and revoke the Beatra device from the console when the credential is no longer trusted.

Risk: Silent verified package updates are enabled by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when explicit update review is required.

Risk: Speech and video generation are paid stages that can consume Beatra credits.

Mitigation: Require explicit approval for each frozen paid payload, use one stable `client_request_id` per logical request, and report only terminal billing facts returned by Beatra.

## Reference(s):

- [Talking-pet workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Beatra Talking Pet Video homepage](https://beatra.ai/skills/talking-pet-video)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/talking-pet-video)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow instructions for inspecting inputs, uploading media, calling Beatra MCP tools, polling tasks, reporting billing facts, and reviewing returned media.]

## Skill Version(s):

0.1.5 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
