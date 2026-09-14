## Description:

多单品融合成一整套 Look。最多 8 张单品图 -> 同一模特身上的完整搭配商拍图，每件单品保真。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and content-production agents use this skill to turn up to 8 product item images into a unified model-worn outfit image for catalog and campaign workflows. It also guides prompt construction, image ordering, visual consistency, dry runs, and quality checks before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to the selected external generation provider, and helper scripts can fetch arbitrary image URLs before upload.

Mitigation: Use vetted local image files where possible, avoid untrusted image URLs, confirm provider data handling, and run the skill in an environment without access to internal services or unrelated credentials.

Risk: Generated outfit composites can omit items, mix colors, alter materials, or place patterns incorrectly.

Mitigation: Use explicit per-image prompt mapping, run dry-run or batch workflows before final generation, and manually verify item count, color, material, pattern placement, and layering before publication.

Risk: Provider credentials are needed for several backends and could be exposed if run in an overly broad environment.

Mitigation: Use scoped API keys through the documented CLI config or environment variables and avoid exposing unrelated credentials to the runtime.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with prompt templates and inline bash commands; executed commands can save generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on up to 8 product item images, optional pose or model references, 3:4 or 1:1 image sizes, 2K default resolution, and batch generation for selection.]

## Skill Version(s):

1.0.9 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
