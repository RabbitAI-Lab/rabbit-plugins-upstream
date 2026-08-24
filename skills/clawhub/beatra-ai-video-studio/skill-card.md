## Description:

Beatra AI Video Studio helps agents plan, generate, animate, edit, extend, and review short AI video clips from text, supplied images, exact frames, multimodal references, or existing footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to turn written concepts or approved source media into short Beatra AI video clips for ads, product stories, social posts, b-roll, transitions, reveals, and cinematic concepts. The skill guides route selection, source admission, paid-task confirmation, task polling, result review, and focused iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a persistent Beatra account token with broad generation and spending scopes.

Mitigation: Install only after reviewing the Beatra authorization flow, keep the credential private, and use Beatra account revocation controls or the bundled uninstall guidance when access should be removed.

Risk: The package can upload selected local media to Beatra for generation tasks.

Mitigation: Inspect source media before upload and send only files the user explicitly approved for Beatra processing.

Risk: Silent package updates are enabled by default during normal use.

Mitigation: Review the automatic-update behavior and disable silent checks with the documented update command when change control is required.

## Reference(s):

- [Beatra AI Video Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra-ai-video-studio)
- [Beatra AI Video Studio Homepage](https://beatra.ai/skills/beatra-ai-video-studio)
- [Intent and routing](artifact/references/intent-and-routing.md)
- [Video recipes](artifact/references/video-recipes.md)
- [Image-assisted video](artifact/references/image-assisted-video.md)
- [Review and iteration](artifact/references/review-and-iteration.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls]

**Output Format:** [Markdown guidance with inline JSON and shell command examples; Beatra API calls return task status, billing fields, and generated media artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses persistent Beatra device-bearer credentials, may upload selected local media to Beatra, and may perform paid generation tasks only after explicit admission and balance confirmation.]

## Skill Version(s):

1.2.4 (source: server release evidence and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
