## Description:

Turn seller-supplied floor-plan facts and an already-written walk-in script into one talking clip per still. This rental walk-in studio turns each authorized still into a 2 to 15s walk-in talking clip from the written line. Use it for rental walk-in videos, listing walk-in talks, and property walk-in talking clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real-estate sellers and listing teams use this skill to turn authorized still images, floor-plan facts, and pre-written walk-in lines into short talking clips for rental or property listings. The skill helps an agent plan the clip list, confirm consent and paid stages, submit Beatra clone, speech, and video work, and recover asynchronous tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra token stored under ~/.beatra.

Mitigation: Install only if that shared credential model is acceptable, keep the token private, and use the documented uninstall or revoke flow when removing Beatra access.

Risk: Authorized media and package or platform installation metadata are sent to Beatra.

Mitigation: Use only media the seller is authorized to provide, confirm likeness and voice rights before paid generation, and avoid submitting private material that is not needed for the clip.

Risk: Silent package updates are enabled by default.

Mitigation: Disable automatic update checks with `python3 scripts/mcp_client.py update --auto off` when silent code updates are not acceptable, and use the documented update check controls before generating paid work.

Risk: Paid clone, speech, and video stages can create duplicate or unintended charges if retried incorrectly.

Mitigation: Show each paid-stage confirmation card first, submit each approved request once with an opaque client_request_id, and recover uncertain tasks with the same identity and unchanged arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/rental-walkin-avatar)
- [Beatra skill homepage](https://beatra.ai/skills/rental-walkin-avatar)
- [Walk-in talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payloads, shell command examples, and generated audio or video artifact files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled clip plan before paid clone, speech, or video stages; final media is delivered as separate files with task, usage, billing, MIME, duration, and size details when available.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
