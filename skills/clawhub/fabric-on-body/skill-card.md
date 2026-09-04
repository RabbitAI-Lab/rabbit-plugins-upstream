## Description:

This skill helps agents generate garment preview images by applying a target fabric sample to an existing garment style reference while preserving silhouette, construction, and camera angle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce production teams use this skill to preview how a garment pattern or style sheet may look when rendered in a different fabric before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided garment and fabric images, prompts, and related metadata may be sent to dLazy or another configured generation provider.

Mitigation: Use explicit local image paths or trusted image URLs, run dry-run first when unsure, and avoid personal or sensitive body photos unless the provider policy and account settings are acceptable.

Risk: Generated fabric replacement images are visual previews and may not represent real fabric hand feel, weight, construction feasibility, or sampling results.

Mitigation: Treat outputs as pre-sampling visual aids and perform human review or physical sampling before production decisions.

## Reference(s):

- [provider-cli.md](references/provider-cli.md)
- [model-flags.md](references/model-flags.md)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands; generated runs save image files such as JPEG outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses garment and fabric image inputs, prompt constraints, quality and size settings, and optional dry-run checks.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
