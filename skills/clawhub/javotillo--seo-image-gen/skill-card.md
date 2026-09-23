## Description:

Generates production-ready SEO image assets such as OG/social previews, blog heroes, schema images, product photos, infographics, favicons, banners, and thumbnails using Gemini through nanobanana tooling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[javotillo](https://clawhub.ai/user/javotillo)

### License/Terms of Use:

MIT

## Use Case:

Developers, SEO practitioners, and content teams use this skill to generate SEO-oriented web and social images, then receive image paths, prompt details, settings, optimization guidance, and schema or Open Graph snippets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image generation can incur API usage costs, especially for batch operations or higher resolutions.

Mitigation: Show estimated cost before generation and use the documented cost tracking commands to log and review usage.

Risk: Generated images, presets, and usage state may be stored locally under user-controlled directories.

Mitigation: Confirm local storage paths before use and avoid sensitive prompts or assets unless local storage is acceptable.

Risk: The skill depends on external Gemini/nanobanana tooling and local helper commands.

Mitigation: Install dependencies intentionally, verify MCP availability before generation, and review fallback helper scripts before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/javotillo/skills/seo-image-gen)
- [Codex Banana](https://github.com/AgriciDaniel/banana-Codex)
- [nanobanana MCP](https://github.com/YCSE/nanobanana-mcp)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Cost Tracking Reference](references/cost-tracking.md)
- [Gemini Image Generation Models](references/gemini-models.md)
- [MCP Tools Reference](references/mcp-tools.md)
- [Post-Processing Pipeline Reference](references/post-processing.md)
- [Brand/Style Presets Reference](references/presets.md)
- [Prompt Engineering Reference](references/prompt-engineering.md)
- [SEO Image Presets](references/seo-image-presets.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown responses with generated image paths, crafted prompts, settings, SEO checklist items, schema or Open Graph snippets, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally by the configured nanobanana tooling; batch generation can increase API cost.]

## Skill Version(s):

1.6.1 (source: artifact/SKILL.md frontmatter metadata.version; server release version 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
