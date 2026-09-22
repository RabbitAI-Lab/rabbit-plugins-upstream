## Description:

Generate platform-tuned social media captions for photography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pfrederiksen](https://clawhub.ai/user/pfrederiksen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and photographers use this skill to turn a shared photo plus context such as location, camera, lens, film stock, subject, or mood into platform-specific captions for social media publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may produce both captions and an added edit-analysis section when a user only expects captions.

Mitigation: Ask the agent to skip edit analysis or limit output to specific platforms when caption-only output is needed.

Risk: Caption quality depends on the accuracy and completeness of the provided photo context.

Mitigation: Provide concrete details such as location, subject, camera, lens, film stock, mood, and any platform targets; avoid asking the agent to invent missing gear or scene details.

## Reference(s):

- [Photo Captions on ClawHub](https://clawhub.ai/pfrederiksen/skills/photo-captions)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with platform-labeled caption sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an additional edit-analysis section and platform-specific constraints such as hashtags, title text, topic suggestions, or gear lines.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
