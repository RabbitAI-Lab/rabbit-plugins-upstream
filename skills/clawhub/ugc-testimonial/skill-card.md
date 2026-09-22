## Description:

Generates UGC-style testimonial scripts, storyboards, and video-generation workflows from product and persona inputs with a casual creator-shot look.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and creative teams use this skill to draft UGC-style product testimonial scripts and storyboards, then run video-generation workflows for ad creatives. The skill is intended for AI-generated demonstrations, not fabricated real buyer reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to the selected AI generation provider.

Mitigation: Use dry-run first, use only approved providers for the data involved, and avoid private customer data, secrets, or unreleased product information in prompts or reference assets.

Risk: Untrusted image URLs or local files may be used as generation inputs.

Mitigation: Provide only trusted image URLs and files, and review the generated request before enabling a paid provider call.

Risk: UGC-style generated content may be mistaken for a genuine buyer testimonial.

Mitigation: Label AI-generated content according to the target platform rules and avoid claims that the output is a real named customer's experience.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI Reference](artifact/references/provider-cli.md)
- [Video Backend Configuration](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, JSON storyboard examples, local file paths, and generated media outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run request summaries, generated MP4 clips or final videos, SRT subtitle files, and concat files depending on the selected workflow.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
