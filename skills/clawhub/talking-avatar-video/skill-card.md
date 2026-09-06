## Description:

Create a talking avatar from one portrait and a short script or speech track. This AI presenter and digital human video workflow can prepare narration with a selected voice or use a supplied recording, then direct a stable talking-head clip with restrained expression, natural movement, clear delivery, and focused lip-sync review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn an authorized portrait plus an approved script or speech track into a single talking-presenter video for explainers, training, lessons, announcements, onboarding, product messages, or social content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared, broad Beatra account credential that can spend credits and access multiple generation and tool categories.

Mitigation: Install only in environments where the credential file is protected, review the requested Beatra connection, and revoke the connected agent from the Beatra Console when no longer needed.

Risk: The package silently checks for and installs newer package code by default before ordinary Beatra commands.

Mitigation: Review the automatic-update behavior and disable silent update checks after installation with `python3 scripts/mcp_client.py update --auto off` when change control is required.

Risk: Narration and video generation are paid actions, and retries or changed inputs can create additional billable work.

Mitigation: Require explicit approval at each paid boundary, reuse the same frozen `client_request_id` only for uncertain delivery of the same request, and report only returned billing facts.

Risk: Talking-avatar output can affect likeness and voice rights and may drift in identity, lip sync, clothing, logos, framing, or background.

Mitigation: Require authorization for the presenter likeness and narration voice before generation, inspect accessible outputs, and describe visible drift or review limits honestly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/talking-avatar-video)
- [Beatra Skill Homepage](https://beatra.ai/skills/talking-avatar-video)
- [Narration-first presenter workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [MCP connection](artifact/references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Beatra task IDs, artifact references, billing facts, and result links when live generation is approved and succeeds.]

## Skill Version(s):

0.2.0 (source: evidence.release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
