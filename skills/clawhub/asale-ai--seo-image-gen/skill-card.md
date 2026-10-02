## Description:

AI image generation for SEO assets: OG/social preview images, blog hero images, schema images, product photography, infographics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to generate SEO-focused image assets, including social preview images, blog hero images, product photography, favicon-style icons, infographics, and schema image guidance through a Gemini-backed nanobanana MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external Banana extension installer, nanobanana MCP server, Gemini API access, and user-provided API credentials.

Mitigation: Verify the extension installer from a trusted source, confirm MCP tool availability before use, and avoid routing confidential prompts or brand assets to external Gemini/MCP services unless approved.

Risk: The evidence security summary flags safety-filter workaround guidance in the artifact.

Mitigation: Treat blocked safety-filter results as a stop or policy review point; do not use rephrasing to preserve prohibited intent.

Risk: Image generation and batch operations may incur API costs or hit rate limits.

Mitigation: Verify current pricing and model configuration before quoting costs, estimate batch cost before generation, and record usage in the available ledger.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/seo-image-gen)
- [Claude Banana source reference](https://github.com/AgriciDaniel/banana-claude)
- [nanobanana MCP package reference](https://github.com/YCSE/nanobanana-mcp)
- [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)
- [Prompt Engineering Reference](references/prompt-engineering.md)
- [Gemini Image Generation Models](references/gemini-models.md)
- [MCP Tools Reference](references/mcp-tools.md)
- [Post-Processing Pipeline Reference](references/post-processing.md)
- [Cost Tracking Reference](references/cost-tracking.md)
- [Brand/Style Presets Reference](references/presets.md)
- [SEO Image Presets](references/seo-image-presets.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with generated image paths, crafted prompts, settings, SEO checklist items, shell commands, and schema or Open Graph snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for image generation and post-processing; actual image files are generated through the configured nanobanana MCP/Gemini tools when available.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter metadata.version is 2.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
