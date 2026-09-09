## Description:

Product Video Ad helps an agent turn product selling points into a multi-shot short advertising video workflow with storyboard prompts, generated clips, concatenation, and subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, commerce operators, and agent developers use this skill to plan and generate 15-30 second product advertising videos from product benefits, reference images, storyboard JSON, brand settings, and provider-backed video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, API keys, and reference media may be sent to the selected generation provider, and one provider path can use an arbitrary Ark-compatible endpoint.

Mitigation: Use only trusted HTTPS provider endpoints, avoid untrusted image URLs, review provider environment variables before execution, and prefer dry-run mode before making generation calls.

Risk: Example brand configuration may contain placeholder assumptions that are unsuitable for real campaigns.

Mitigation: Edit the example brand.yaml before production use and confirm each storyboard prompt, reference image, and caption with the campaign owner before generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI Reference](references/provider-cli.md)
- [Video Backend Configuration](references/video-backends.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [Related main-image-video Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/main-image-video/skill.md)
- [Related ugc-testimonial Skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/ugc-testimonial/skill.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON storyboard examples, YAML brand configuration, bash commands, and generated MP4/SRT output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run review before provider calls; generated storyboard runs can produce per-shot MP4 files, captions.srt, concat.txt, final.mp4, and final-sub.mp4.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
