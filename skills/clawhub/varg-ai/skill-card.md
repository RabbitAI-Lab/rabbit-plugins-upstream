## Description:

Generate AI videos, images, speech, and music with varg using cloud rendering via curl or local rendering with bun and ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securityqq](https://clawhub.ai/user/securityqq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to create AI-generated videos, images, speech, music, captions, and rendered media workflows through varg cloud APIs or a local bun and ffmpeg setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles long-lived VARG_API_KEY credentials and may save them to local files.

Mitigation: Keep API keys in environment variables or protected credential files, avoid committing .env files, and require explicit user approval before saving credentials.

Risk: The skill can start paid render jobs or create checkout links for varg credits.

Mitigation: Check balance and estimate cost before rendering, use preview or lower-cost models while iterating, and require explicit approval before billable renders or checkout creation.

Risk: Render inputs and uploaded files may be sent to a paid remote media service.

Mitigation: Avoid sending secrets, private source code, internal URLs, customer data, or personal photos unless the user explicitly approves the upload.

## Reference(s):

- [varg homepage](https://varg.ai)
- [Cloud Render Mode](references/cloud-render.md)
- [Local Render Mode](references/local-render.md)
- [varg API Reference (v2)](references/gateway-api.md)
- [Model Catalog](references/models.md)
- [Component Reference](references/components.md)
- [Recipes & Patterns](references/recipes.md)
- [Prompt Engineering Guide](references/prompting.md)
- [Common Errors & Debugging](references/common-errors.md)
- [BYOK (Bring Your Own Key)](references/byok.md)
- [Complete Templates](references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with TypeScript/TSX, JSON, and bash snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API calls, render templates, setup steps, and media-generation guidance; generated media is created by the external varg service or local render tooling.]

## Skill Version(s):

2.0.9 (source: server release evidence; artifact frontmatter reports 2.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
