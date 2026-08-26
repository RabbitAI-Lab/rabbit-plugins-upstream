## Description:

AI电商专家｜电商文生视频 helps ecommerce content, advertising, operations, brand, livestream commerce, and seeding teams turn product facts and scripts into commercial short-video generation tasks through the IMIVA MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and content operators use this skill to prepare IMIVA MCP parameters for text-to-video product advertising workflows, including budget checks, task creation, task lookup, and result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned external npm package with an MCP token and the user's process environment.

Mitigation: Install only when the IMIVA/@infimind package and remote service are trusted; prefer pinning the package version, running from a shell without unrelated secrets, and using a limited, revocable MCP token.

Risk: Video generation tasks may consume platform credits and upload local or HTTPS media assets.

Mitigation: Use dry-run checks when available, confirm estimated credits and media inputs with the user, and set explicit task limits before creating paid tasks.

## Reference(s):

- [IMIVA homepage](https://imiva.ecpro.com/)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-ecommerce-expert-ecommerce-text-to-video)
- [MCP configuration example](references/mcp-config.example.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the IMIVA MCP through an external npm package and can prepare task arguments for video generation, credit checks, and task queries.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
