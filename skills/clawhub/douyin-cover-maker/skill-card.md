## Description:

Create a Douyin cover or vertical short-video cover from a video topic, hook, script, portrait, product photo, or reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to turn a confirmed Douyin topic, hook, script, key frame, product photo, portrait, or reference image into one publish-ready vertical cover with a clear focal subject and headline-safe composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra authorization grants broad account capabilities and stores a shared bearer token in ~/.beatra.

Mitigation: Install only where broad Beatra account access is acceptable, keep the token out of logs and chat, and disconnect through the bundled uninstall workflow or Beatra Console when access is no longer needed.

Risk: Automatic updates are enabled by default and can replace package-owned files without a separate confirmation.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when package replacement should require manual review.

Risk: Paid generation requests can create duplicate or changed billable work if retried with different inputs.

Mitigation: Confirm the final prompt, canvas, references, model, controls, and count before submission, then reuse the same client_request_id only for byte-equivalent recovery retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-cover-maker)
- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown with JSON request bodies, shell commands, task identifiers, billing fields, and artifact links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates one paid image-generation or image-edit task by default and reports only returned task, artifact, usage, and billing fields.]

## Skill Version(s):

0.1.3 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
