## Description:

Helps turn a finished song excerpt and visual direction into a short AI-generated music video clip or animated cover-art teaser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Artists, music marketers, and creators use this skill to plan and generate short promotional clips from cleared music excerpts, with optional cover-art animation and visual direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra Device Token grants broad access across installed Beatra skills.

Mitigation: Keep ~/.beatra/credentials.json private and remove the shared connection using the uninstall workflow when no longer needed.

Risk: The bundled client silently updates package files by default.

Mitigation: Review the update channel before installation; disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if unwanted.

Risk: Uploaded media and paid generation requests are processed by Beatra and can spend wallet credits.

Mitigation: Upload only approved media and confirm each paid request and its estimated cost before submission.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/ai-music-video-clip-maker)
- [Music video clip workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with commands and links to generated clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation is asynchronous and may consume paid credits.]

## Skill Version(s):

0.2.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
