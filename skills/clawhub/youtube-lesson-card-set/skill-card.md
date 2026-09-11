## Description:

Turn public YouTube lesson captions into a set of 4 to 8 takeaway cards. This lesson card studio reads the lesson captions, pulls the key points, and lays out one card per point for lessons and tutorial videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education content creators use this skill to turn public YouTube lesson captions or pasted caption lines into 4 to 8 caption-backed takeaway card stills. It helps an agent plan the card set, confirm paid caption lookup or image generation stages, and report task results and billing facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary classifies the release as suspicious because it uses broad shared account authority and silent self-updating code.

Mitigation: Review the skill before installation, install only when comfortable granting the shared Beatra device credential, and consider disabling automatic updates with the documented update --auto off command.

Risk: Uploaded brand stills and lesson inputs may contain sensitive content.

Mitigation: Use only non-sensitive brand stills and caption content, and revoke the device from the Beatra Console when the agent should no longer be connected.

Risk: Paid lookup and image-generation stages can charge credits or create duplicate work if retried incorrectly.

Mitigation: Require a separate user confirmation for each paid stage, preserve the client_request_id for uncertain delivery, and retry only byte-identical requests with the same request identity.

## Reference(s):

- [YouTube Lesson Card Set on ClawHub](https://clawhub.ai/beatra-ai/skills/youtube-lesson-card-set)
- [Beatra Skill Homepage](https://beatra.ai/skills/youtube-lesson-card-set)
- [Lesson Knowledge-Point Still Workflow](references/workflow.md)
- [YouTube Lesson Caption Lookup](references/caption-lookup.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces caption-to-card plans, confirmation cards, task status summaries, and image-generation guidance; final generated images are returned by the connected Beatra tools.]

## Skill Version(s):

0.1.3 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
