## Description:

Use when someone wants a montage with transitions between shots - an action-sequence reel or multi-scene piece where narration is optional.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan, generate, review, and assemble multi-scene transition reels from start/end still pairs, optional user images, and generated video clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unpinned `npx skills add` install path may resolve to a moving Pruna skill release.

Mitigation: Install only from the server-resolved `pruna-ai` publisher profile and review the selected release before use.

Risk: Selected input images are uploaded to the generation service during still and video creation.

Mitigation: Use only images approved for third-party processing and avoid sensitive or restricted media.

Risk: Paid video generation can consume credits if review gates are skipped.

Mitigation: Require the documented approve plan, approve stills, and approve clips gates before generating or assembling final media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/visual-transition-reel)
- [Example prompt](artifact/example-prompt.md)
- [Transition plan template](artifact/templates/transition-plan.template.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration, shell commands, code]

**Output Format:** [Markdown guidance with JSON plan data and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates local still, clip, plan, and assembled video files with explicit approval gates before paid video generation.]

## Skill Version(s):

1.0.11 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
