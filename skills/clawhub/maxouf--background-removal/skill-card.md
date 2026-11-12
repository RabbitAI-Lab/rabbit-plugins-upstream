## Description:

Remove the background from one image or thousands and deliver a transparent PNG or WebP cutout per image (optional black-and-white mask), from URLs, Drive/Dropbox links, uploads or another Actor's dataset, with width, height and status per item. Use when the user says "background removal", "remove the background from these photos", "background removal API", "transparent PNG cutouts for my product photos", "cut out the subject", "bulk background remover", or "remove bg from this dataset of images". Compares three ways to do it (Sherwood Background Remover API on Apify, the free local rembg CLI, a direct fal.ai or Replicate call) and picks one from volume, privacy and whether the user already has a model key; notes that remove.bg is closing. Out of scope: replacing the background with a generated scene, removing objects inside the subject, video matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxouf](https://clawhub.ai/user/maxouf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to choose a background-removal method and process individual images or batches into transparent cutouts, with optional masks and per-image results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags advice that may broaden image access to anyone with a link, without explaining the privacy impact.

Mitigation: Before using shared links for private images, confirm that the access change is acceptable; use the local rembg option when images must stay on-device.

Risk: The security scan was partial, so some components and instruction checks were not fully assessed.

Mitigation: Treat the scan as incomplete and review the skill and selected tools before use.

## Reference(s):

- [Skill homepage](https://github.com/maxouf/sherwood-skills/tree/main/skills/background-removal)
- [Background removal gotchas](references/gotchas.md)
- [Apify MCP tool](https://mcp.apify.com/?tools=sherwood/background-remover-batch)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, CSV files, Image files]

**Output Format:** [Markdown guidance and commands; JSON inputs; CSV results; transparent PNG or WebP cutouts and optional PNG masks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-image status, dimensions, input and output references, optional mask reference, and errors; batch size is bounded by maxImages.]

## Skill Version(s):

1.0.0 (source: skill frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
