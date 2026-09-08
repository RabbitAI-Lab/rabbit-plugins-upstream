## Description:

Use when someone wants a multi-part story with voiceover - episodic B-roll, chaptered promo, or several linked video scenes without on-camera dialogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and generate narrated multi-scene video stories, including scene tables, still-image anchors, narration audio, video clips, and final assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prerequisite generation skills may change behavior or terms after installation.

Mitigation: Review prerequisite Pruna skills before installing and prefer pinned or known-good versions.

Risk: API-backed image, audio, or video generation can consume paid credits before the user has confirmed the intended scene plan.

Mitigation: Use the documented approval gates and proceed with cost-bearing generation only after the plan and required review steps are confirmed.

Risk: Narration-led video clips can truncate when scene audio exceeds the API duration cap.

Mitigation: Check each narration file duration and shorten, speed up, or split lines before sending clips to video generation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, JSON snippets, and inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scene manifests, media URLs, generated file paths, and ffmpeg command proposals.]

## Skill Version(s):

1.0.11 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
