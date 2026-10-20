## Description:

Guides an agent in removing text, watermarks, and promotional overlays from images while reconstructing obscured backgrounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and commerce teams use the skill to prepare cleaner images by removing overlays and reconstructing covered areas before reuse in other workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to the configured cloud provider.

Mitigation: Use --dry-run and --provider to review routing; avoid uploading private images without authorization.

Risk: Removing ownership marks or required labels could enable misuse.

Mitigation: Edit only images you have rights to use; do not remove copyright, certification, or safety markings to misrepresent them.

Risk: AI reconstruction can change details outside the removed overlay.

Mitigation: Review the edited image against the original, especially products and perspective; use pixel-accurate editing when exact fidelity matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/remove-watermark)
- [Model flags](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save edited images locally; reconstructed regions are inferred, not pixel-exact repairs.]

## Skill Version(s):

1.0.24 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
