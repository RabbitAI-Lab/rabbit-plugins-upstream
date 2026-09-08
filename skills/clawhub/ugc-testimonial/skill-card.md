## Description:

Generates UGC-style product testimonial scripts, storyboards, and video-generation commands from a product and buyer persona, aiming for a casual selfie-style promotional clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and ecommerce teams use this skill to turn product details and buyer personas into short UGC-style testimonial concepts, scripts, storyboard shots, subtitles, and generation commands. It is intended for promotional content workflows where AI-generated or simulated testimonial content is reviewed and disclosed according to platform rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard and brand configuration may reference arbitrary local files or URLs that are sent to a selected generation provider.

Mitigation: Review every image path and URL before running real provider calls, use trusted configs only, and operate from a restricted working directory without sensitive files.

Risk: Generated outputs may be written outside the intended folder if save or output paths are set carelessly.

Mitigation: Use a dedicated output directory, review save paths during dry-run, and inspect generated files before sharing or publishing them.

Risk: UGC-style AI content can mislead viewers if presented as a real buyer's genuine testimonial.

Mitigation: Label AI-generated or simulated content as required, avoid claims of real customer experience, and confirm the target platform's disclosure rules before publishing.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/dlazyai/skills/ugc-testimonial)
- [Backend invocation reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, files, guidance]

**Output Format:** [Markdown guidance with bash and JSON examples; generation runs can produce MP4 files, SRT subtitles, concat manifests, and JSON status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run previews, explicit video model selection, storyboard input, brand configuration, and optional subtitle attachment.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
