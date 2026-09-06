## Description:

Seedancer is a Chinese-first AI filmmaking workflow skill that turns scripts and shot briefs into production-ready image prompts, video prompts, shot plans, asset sheets, and bilingual JSON or Markdown deliverables for AI video and image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taosiuman](https://clawhub.ai/user/taosiuman)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, filmmakers, and agent operators use this skill to convert scripts or single-shot ideas into structured AI video and image generation prompts, pre-production artifacts, continuity checks, retake diagnostics, and delivery manifests. It is most useful when a workflow needs detailed cinematic planning, prompt quality gates, bilingual output, or reusable production documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented API example may send scripts, production details, personal data, or proprietary assets to a remote processing path.

Mitigation: Use non-confidential briefs or obtain approval before sending sensitive material through that API path.

Risk: The skill produces detailed prompts and production guidance that may be reused in downstream image or video generation tools.

Mitigation: Review generated prompts, references, and asset descriptions for rights, privacy, safety, and platform-policy fit before external use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/taosiuman/skills/seedancer)
- [README](README.md)
- [JSON API Output Mode](references/json-api-mode.md)
- [Deliverable System](references/deliverable-system.md)
- [Scene Prototypes](references/scene-prototypes.md)
- [Camera-Emotion Sync](references/camera-emotion-sync.md)
- [Lighting Rules](references/lighting-rules.md)
- [Failure Codes](references/failure-codes.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown production plans and prompt files, with optional bilingual JSON arrays and occasional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-first workflow; optional JSON mode returns English and Chinese prompt objects, with the Chinese prompt capped at 1,800 characters.]

## Skill Version(s):

7.0.2 (source: frontmatter, VERSION, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
