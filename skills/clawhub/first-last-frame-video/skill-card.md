## Description:

Helps create and review a short video transition between two approved endpoint images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan a directed transition from an approved first image to an approved last image, generate one clip, and review its endpoint fidelity and motion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared device connection grants broad Beatra account and tool access across Beatra skills.

Mitigation: Authorize only when comfortable with shared access, protect the device connection, and review shared-connection behavior before uninstalling.

Risk: Package updates are enabled by default and can replace code without a separate confirmation.

Mitigation: Review the update policy and disable automatic updates with the documented control if changes must be reviewed first.

Risk: Video generation spends credits and estimates can differ from final charges.

Mitigation: Review the live estimate and approve the paid transition before submission; check the completed task for the final charge.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/first-last-frame-video)
- [Beatra skill page](https://beatra.ai/skills/first-last-frame-video)
- [First-and-last-frame workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Video artifact links]

**Output Format:** [Markdown text with transition plan, approval details, and returned video links or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports actual task results and charges when available; video generation requires credits and explicit approval.]

## Skill Version(s):

0.1.9 (source: server release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
