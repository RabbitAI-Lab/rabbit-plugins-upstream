## Description:

Create a Douyin cover or vertical short-video cover from a video topic, hook, script, portrait, product photo, or reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to turn a short-video idea, script hook, portrait, product photo, key-frame screenshot, or accepted draft into one publish-ready Douyin or vertical short-video cover. The workflow helps an agent prepare a concise cover brief, confirm paid Beatra generation work, submit a single remote image task, track the result, and report returned artifacts and billing fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with broad media and wallet-related scope.

Mitigation: Install only where that authorization scope is acceptable, keep the credential in the documented private file location, and revoke or uninstall through the bundled disconnect flow when access is no longer needed.

Risk: Remote cover generation consumes Beatra credits and can create duplicate paid work if retries are changed.

Mitigation: Confirm paid work before submission, use one opaque client_request_id per unchanged request, and retry only byte-equivalent payloads with the same request identity after uncertain transport failures.

Risk: The bundled client silently checks for and applies package updates by default.

Mitigation: Use the documented update controls to disable automatic checks where silent package replacement is not acceptable, and rely on the package's checksum and fixed-source update validation when updates remain enabled.

Risk: Selected local image files may be uploaded to Beatra for transform or edit workflows.

Mitigation: Upload only files the user intentionally provides for the cover task, avoid including sensitive content, and preserve artifact references only as needed for the confirmed workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/douyin-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-cover-maker)
- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and remote task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one Beatra image task request and returns artifact links, observed dimensions, task ID, resolved model, and billing fields when available.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
