## Description:

Remove backgrounds from images with BiRefNet through the inference.sh CLI, producing transparent PNG outputs for product photos, portraits, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okaris](https://clawhub.ai/user/okaris)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to run inference.sh image workflows for background removal, background changes, and transparent cutouts. The documented use cases include e-commerce product photos, portraits, marketing assets, social media profile images, and design compositions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote installers and optional unpinned skill installs can expand trust beyond the stated background-removal task.

Mitigation: Review the skill before installing, prefer a manual version-pinned CLI download with checksum or signature verification, and avoid optional broad npx skill installs unless those extra remote skills are intended and trusted.

## Reference(s):

- [Skill Page](https://clawhub.ai/okaris/skills/background-removal)
- [inference.sh](https://inference.sh)
- [inference.sh CLI Checksums](https://dist.inference.sh/cli/checksums.txt)
- [Running Apps](https://inference.sh/docs/apps/running)
- [Image Generation Example](https://inference.sh/docs/examples/image-generation)
- [Apps Overview](https://inference.sh/docs/apps/overview)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referenced inference.sh apps return image outputs, including PNG files with transparent backgrounds.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
