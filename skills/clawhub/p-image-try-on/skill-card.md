## Description:

Use when someone wants virtual try-on: dress a person in clothes from reference photos for fashion or ecommerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce or fashion teams use this skill to prepare and run virtual try-on jobs that place supplied garments onto a supplied person image through Pruna's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends unpinned auto-accepted installs for prerequisite PrunaAI skills.

Mitigation: Review and preferably pin prerequisite skill installs before use, and avoid auto-accepting installs where manual review is feasible.

Risk: Virtual try-on requires sending identifiable person photos and garment assets to a third-party API.

Mitigation: Upload only images the user has permission to share, use a scoped API key, and review Pruna's privacy, retention, and deletion terms before using real customer or employee photos.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-try-on)
- [Canonical output: editorial seated with artistic shirt](https://replicate.com/p/p47vaj1f91rmw0cyt4er0z2zd4)
- [Canonical output: complex collaged suit](https://replicate.com/p/tf7gqansnnrmt0cyt4j8mpx1c8)
- [Canonical output: mirror selfie with cap and logo tee](https://replicate.com/p/hp60wyj355rmy0cyt4psnc2mh0)
- [Canonical output: multi-garment streetwear stack](https://replicate.com/p/bak21xr79srmr0cyt52tap1nw8)
- [Canonical output: pleated blouse golden-hour portrait](https://replicate.com/p/g9hd22x26drmr0cytmtsx11c5g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and user-provided person_image and garment_images URLs; output images are produced by the Pruna API.]

## Skill Version(s):

1.0.12 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
