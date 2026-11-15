## Description:

Generates single images or batches of images from text prompts and helps choose a hosted or local workflow based on the user's model preferences, budget, volume, and hardware.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxouf](https://clawhub.ai/user/maxouf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can turn one prompt or a prompt list into generated images, then receive image URLs and result metadata. The skill helps select a hosted image service or a local setup based on the user's volume, preferred model, budget, and hardware.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts may contain confidential material that is processed by an external image service.

Mitigation: Avoid sending sensitive prompts unless the user is comfortable with the selected service processing them.

Risk: Generated images may be shared with downstream actors or included in scheduled processing.

Mitigation: Check downstream sharing and scheduling settings before chaining or scheduling image workflows.

Risk: Batch size, image variations, and larger dimensions can increase per-run charges.

Mitigation: Estimate the total cost, bound prompts and variations, and set a per-run spending limit where the service supports it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maxouf/skills/text-to-image)
- [Skill homepage listed in Clawdis metadata](https://github.com/maxouf/sherwood-skills/tree/main/skills/text-to-image)
- [Apify MCP tool endpoint](https://mcp.apify.com/?tools=sherwood/image-generator-batch)
- [Cost and recovery notes](artifact/references/gotchas.md)

## Skill Output:

**Output Type(s):** [Generated images, Image URLs, CSV files, JSON dataset items, Usage guidance, Shell commands, Python code]

**Output Format:** [Image URLs and metadata in CSV or JSON, with Markdown guidance and shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results can include prompt, dimensions, seed, format, status, and error details; batch size and variations are configurable.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
