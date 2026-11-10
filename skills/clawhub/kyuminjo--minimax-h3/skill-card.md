## Description:

Generate videos with MiniMax H3, the Hailuo video model, via the PopNow API: expressive text-to-video and image-to-video with audio, up to 30 seconds or 2K, plus HighSpeed, Lite, Max and LoRA variants. Exact USD quotes first. Use when the user asks for Hailuo, MiniMax video or a low-cost AI video clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyuminjo](https://clawhub.ai/user/kyuminjo)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to create text-to-video, image-to-video, reference-based, or extended clips with MiniMax H3 through PopNow. It quotes the maximum USD charge before creation and returns task status and output links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video generation can spend from the prepaid API USD balance.

Mitigation: Present the exact quote and obtain explicit approval of maxChargeUsd before creating a task.

Risk: Prompts and reference media URLs are sent to PopNow and the generation provider; host logs may retain command arguments, and provider-side data retention was not tested.

Mitigation: Avoid sensitive prompts and URLs, submit only material the user has rights to use, and keep the API key in secret settings rather than command arguments.

## Reference(s):

- [MiniMax H3 model page](https://popnow.ai/models/minimax-h3)
- [PopNow task API documentation](https://popnow.ai/docs/tasks)
- [ClawHub skill release](https://clawhub.ai/kyuminjo/skills/minimax-h3)

## Skill Output:

**Output Type(s):** [Video, API Calls, Text]

**Output Format:** [Generated video available through provider output links, with JSON quote and task-status data]

**Output Parameters:** [Variable, according to the selected model's input schema]

**Other Properties Related to Output:** [Task creation requires explicit approval of the quoted maximum USD charge.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
