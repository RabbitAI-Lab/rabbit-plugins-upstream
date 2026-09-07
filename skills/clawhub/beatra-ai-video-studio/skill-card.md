## Description:

Plan and create short AI videos from a written shot, a supplied image, exact first and last frames, multimodal references, or existing footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, submit, monitor, and review short AI video work through Beatra, including text-to-video, image-to-video, reference-guided generation, editing, and extension for ads, product stories, social clips, b-roll, transitions, reveals, and cinematic concepts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent local Beatra device credential with broad account authority.

Mitigation: Install only where Beatra is trusted, use accounts with the minimum needed permissions and credits, and revoke the connected agent when access is no longer required.

Risk: The skill can upload user-provided media and use paid credit-spending Beatra operations.

Mitigation: Avoid sensitive media, require explicit confirmation before paid video stages, and keep account balances limited to the expected work.

Risk: Default-on package self-updates can silently replace local package files from Beatra's update channel.

Mitigation: Review the update behavior before managed or sensitive deployments and disable automatic updates for routine use when change control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/beatra-ai-video-studio)
- [Beatra skill homepage](https://beatra.ai/skills/beatra-ai-video-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Shot design](references/shot-design.md)
- [Image-assisted video](references/image-assisted-video.md)
- [Video recipes](references/video-recipes.md)
- [Review and iteration](references/review-and-iteration.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task status, artifact links, billing details, media review notes, and next-step recommendations after tool execution.]

## Skill Version(s):

1.2.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
