## Description:

Generates SEO-focused images such as OG/social previews, blog hero images, schema images, product photos, infographics, favicons, banners, and thumbnails using Gemini via nanobanana-mcp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and SEO practitioners use this skill to generate web and social image assets with SEO-oriented settings. It also guides post-generation alt text, file naming, WebP conversion, schema markup, and Open Graph metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Safety-filter workaround language could encourage bypass-style rephrasing.

Mitigation: Rewrite blocked-content handling to require safe redirection and policy-compliant alternatives rather than bypass-oriented prompt changes.

Risk: The skill relies on external Gemini/nanobanana services and credentialed API access.

Mitigation: Verify tool availability and credentials before use, protect API keys, and avoid sending sensitive or unapproved content to external services.

Risk: Generated images and cost ledgers may be stored locally.

Mitigation: Tell users where files and cost records are saved, apply local retention rules, and clean up generated assets when they are no longer needed.

Risk: Batch image generation can create unexpected cost exposure.

Mitigation: Estimate cost before batch runs and verify current pricing against the installed tool configuration or provider pricing documentation.

Risk: Model aliases, resolution support, and pricing may be stale or package-specific.

Mitigation: Confirm model IDs, supported parameters, and pricing in the installed MCP package and current provider documentation before relying on them.

## Reference(s):

- [Skill page](https://clawhub.ai/asale-ai/skills/seo-image-gen)
- [Claude Banana](https://github.com/AgriciDaniel/banana-claude)
- [nanobanana-mcp](https://github.com/YCSE/nanobanana-mcp)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Cost Tracking Reference](references/cost-tracking.md)
- [Gemini Image Generation Models](references/gemini-models.md)
- [MCP Tools Reference](references/mcp-tools.md)
- [Post-Processing Pipeline Reference](references/post-processing.md)
- [Brand/Style Presets Reference](references/presets.md)
- [Prompt Engineering Reference](references/prompt-engineering.md)
- [SEO Image Presets](references/seo-image-presets.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Image files]

**Output Format:** [Markdown with generated image paths, crafted prompts, model settings, SEO checklist items, shell snippets, and JSON or HTML metadata snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call configured Gemini/nanobanana image-generation tools and save generated images or cost records locally.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter metadata lists 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
