## Description:

Generates UGC-style product testimonial scripts, storyboards, and video outputs from product and persona inputs for influencer-style recommendation creatives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, commerce teams, and creative operators use this skill to create AI-generated UGC-style product testimonial scripts, storyboarded shots, subtitles, and video assets for ad creative testing. Outputs should be reviewed so they are not presented as real customer testimonials and are disclosed as AI-generated where platform rules require it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided prompts, product details, and referenced images may be sent to the configured AI generation provider.

Mitigation: Use --dry-run first, choose the provider intentionally, and avoid sending sensitive or unauthorized assets.

Risk: AI-generated UGC-style output could be mistaken for a real customer testimonial or undisclosed endorsement.

Mitigation: Do not claim generated people are real buyers, verify product claims, and disclose AI-generated content where platform rules require it.

Risk: Video model limitations can produce poor lip sync, inconsistent faces, or misleading visuals.

Mitigation: Use voiceover rather than synchronous speech, lock persona references where available, keep talking-head clips short, and review outputs before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [Brand Kit Reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with JSON storyboard examples, bash commands, subtitles, and locally saved media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send prompts, product details, and referenced images to the configured generation provider; dry-run mode previews requests before generation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
