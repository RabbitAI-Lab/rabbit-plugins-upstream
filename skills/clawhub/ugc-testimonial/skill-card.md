## Description:

Creates UGC-style product recommendation scripts, shot lists, and short videos with a casual selfie aesthetic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to draft persona-based product recommendation scripts and generate UGC-style video shots for advertising, with optional subtitles and voiceover added during editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced product or model images may be sent to the selected cloud provider.

Mitigation: Use --dry-run first and exclude sensitive images and private customer data from prompts and inputs.

Risk: UGC-style videos may be mistaken for genuine customer testimonials.

Mitigation: Do not present generated personas as real buyers; review claims and follow the target platform's AI-content labeling requirements.

Risk: Example persona and model settings may not match approved brand guidance.

Mitigation: Replace the example settings with approved brand assets and review the script before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Provider CLI guide](artifact/references/provider-cli.md)
- [Video backend guide](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Video files, Subtitles]

**Output Format:** [Product scripts and shot lists in text or Markdown; generated MP4 clips and optional SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation requires a chosen cloud model; generated shots do not provide reliable lip synchronization.]

## Skill Version(s):

1.0.18 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
