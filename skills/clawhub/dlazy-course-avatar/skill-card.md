## Description:

Knowledge-course and online-teaching avatar lecturer workflow with landscape base-portrait recipes and a slide-first pipeline for producing paid-course, training, and knowledge-sharing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, trainers, and course teams use this skill to plan and generate digital-human course videos from lectures, slides, scripts, voiceover, and avatar footage while controlling avatar screen time and cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, media, and uploaded course documents may be processed by the dLazy cloud service.

Mitigation: Review privacy requirements for course materials before use and avoid uploading sensitive content unless the service terms and data handling are acceptable.

Risk: The dLazy API key may be stored locally after login.

Mitigation: Use the documented configuration location or DLAZY_API_KEY environment variable deliberately, restrict key access, and rotate keys if exposure is suspected.

Risk: Avatar video workflows can create AI-generated lecturer content that may require disclosure or platform-specific labeling.

Mitigation: Apply required AI-generated content labels and review course marketing, legal, and platform disclosure requirements before publishing.

Risk: Incorrect command parameters, oversized prompts, or unsuitable source images can waste paid generation credits or produce unusable video.

Mitigation: Use dry runs, confirm current CLI flags, keep prompts within model limits, and inspect base portraits before driving longer avatar segments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [Artifact: SKILL.md](artifact/SKILL.md)
- [Artifact: pipeline.md](artifact/pipeline.md)
- [Artifact: recipes.md](artifact/recipes.md)
- [Artifact: troubleshooting.md](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose dLazy CLI commands, prompt payloads, and video assembly steps for user review before execution.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
