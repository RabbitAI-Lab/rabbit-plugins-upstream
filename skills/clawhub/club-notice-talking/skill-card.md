## Description:

Turns a teacher-supplied club activity script and authorized stills into separate 2 to 15 second talking clips, one per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, club advisors, and supporting agents use this skill to plan and generate short club activity announcement clips from authorized still images and user-supplied activity script points. It keeps planning separate from paid clone, speech, and video generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad media, artifact, task, voice, and spending capabilities.

Mitigation: Install only where that account authority is acceptable, review the approval page carefully, and keep the local credential private.

Risk: The bundled client can silently self-update code.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if unattended code replacement is not acceptable.

Risk: Paid clone, speech, and video tasks can consume credits, and duplicate changed submissions can create new billable work.

Mitigation: Confirm each paid stage separately, use one opaque `client_request_id` per approved request, and retry uncertain paid calls only with identical arguments.

Risk: Talking clips may involve a person's likeness or cloned voice.

Mitigation: Use only authorized stills and voice samples, and require explicit likeness and voice rights before cloning or animating.

## Reference(s):

- [Activity-script talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra skill homepage](https://beatra.ai/skills/club-notice-talking)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/club-notice-talking)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets; approved Beatra tasks can return generated media artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled slot list before paid work, then separate 2 to 15 second talking clips per approved still; clips are not stitched.]

## Skill Version(s):

0.1.3 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
