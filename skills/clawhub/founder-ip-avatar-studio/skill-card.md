## Description:

Turn one authorized founder or expert portrait and a weekly script into a talking-head IP video in that person's likeness and voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, founders, experts, and brand teams use this skill through an agent to create authorized recurring talking-head avatar videos from a portrait and approved script or audio. The workflow covers consent checks, voice cloning or catalog voice selection, narration, paid video generation, result review, and recovery from interrupted tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization that can upload media, create paid generation tasks, and spend credits.

Mitigation: Install only when that authorization is acceptable, keep the token local, and revoke the device in the Beatra Console or run the uninstall flow when finished.

Risk: Silent automatic updates are enabled by default for installed package files.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required.

Risk: Avatar video and voice clone work can misuse likeness or voice rights if authorization is missing.

Mitigation: Confirm rights and consent before cloning voices, synthesizing speech, or generating video; stop when authorization is absent.

Risk: Paid generation steps can create duplicate charges if uncertain requests are retried with changed payloads.

Mitigation: Use one frozen `client_request_id` per paid stage and retry only the identical payload when delivery is uncertain.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/founder-ip-avatar-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/founder-ip-avatar-studio)
- [Founder avatar workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent through Beatra task creation, polling, billing review, and delivery of returned video clips; paid generation steps require explicit user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
