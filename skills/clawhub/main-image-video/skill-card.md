## Description:

Turns a product's static main image into a short listing video with controllable camera movement and subtle material motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and operators use the skill to create short product listing videos from existing product photos, with a motion prompt and optional brand styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected cloud generation provider; ClawScan reports provider-routing and privacy concerns, and scan coverage is incomplete.

Mitigation: Before use, confirm which provider receives the inputs and that its access and data use fit your needs; review the components that were only partially inspected.

## Reference(s):

- [Video backend configuration](artifact/references/video-backends.md)
- [Provider and data-flow guide](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Video files, Subtitle files]

**Output Format:** [MP4 video clips; optional SRT subtitles and storyboard JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically a 3–5 second listing clip; duration and supported models vary by provider. Storyboard mode can join multiple shots and add captions.]

## Skill Version(s):

1.0.28 (source: SKILL.md frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
