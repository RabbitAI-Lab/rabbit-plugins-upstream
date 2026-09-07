## Description:

Continue one short source video before or after its existing action by planning a continuity state, submitting a Beatra video-extension task, and reviewing the returned clip for visual and audio continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and external users use this skill to extend a single short video clip forward or backward while preserving subject, motion, camera, lighting, audio intent, and final-duration constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broad paid-generation, wallet, artifact, and task authority.

Mitigation: Install only in a trusted environment, keep the credential local, and revoke the Beatra device in the Console when access is no longer needed.

Risk: The bundled client silently checks for and installs newer package code by default.

Mitigation: Review the automatic-update behavior before installation and disable silent updates with the documented update command when change control is required.

Risk: Video extension is paid work, and duplicated submissions can create duplicate tasks or charges.

Mitigation: Require an admission card and user confirmation before submission, use one stable client_request_id per paid request, and recover uncertain results before creating changed work.

## Reference(s):

- [AI Video Continuation ClawHub listing](https://clawhub.ai/beatra-ai/skills/ai-video-continuation)
- [Beatra AI Video Continuation homepage](https://beatra.ai/skills/ai-video-continuation)
- [Video continuation workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides task submission, polling, recovery, cancellation, and returned artifact reporting; no fixed token cap is specified.]

## Skill Version(s):

0.1.7 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
