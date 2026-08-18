## Description:

Seedancer is an AIGC filmmaking director workflow that helps agents move from script analysis and pre-production assets to multi-shot image/video prompt planning, project state management, revisions, and delivery notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and production teams use Seedancer to translate scripts or shot requests into structured AIGC film production workflows, including pre-production analysis, asset planning, image/video prompts, retake diagnostics, and delivery artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found prompt guidance that appears to avoid moderation signals.

Mitigation: Review or remove the moderation-avoidance wording before installation and supervise generated prompts before submitting them to external image or video platforms.

Risk: Scripts, character references, and production assets may be processed by the assistant and any selected generation tools.

Mitigation: Only provide material that is acceptable for processing by the assistant and by the external image or video tools selected for the workflow.

Risk: Generated prompts, shot plans, and diagnostics may be incorrect, misleading, or unsuitable for a production context.

Mitigation: Review generated outputs before execution, publication, or submission to external services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/seedancer)
- [README](README.md)
- [Release notes](release-notes.md)
- [Story analysis](references/story-analysis.md)
- [Creative baseline](references/creative-baseline.md)
- [Character assets](references/character-assets.md)
- [Prop assets](references/prop-assets.md)
- [CINEDANCE video prompt system](references/cinedance-video-prompt.md)
- [LIRA image prompt system](references/lira-image-prompt.md)
- [Failure codes](references/failure-codes.md)
- [Deliverable system](references/deliverable-system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured tables, prompt blocks, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include image and video prompt specifications, shot plans, asset lists, project state handoffs, and retake diagnostics.]

## Skill Version(s):

5.0.0 (source: SKILL.md frontmatter, VERSION, release evidence; released 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
