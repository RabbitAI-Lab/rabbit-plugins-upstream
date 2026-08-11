## Description:

Generates and edits images or videos from prompts using routed providers such as GPT Image 2, Nanobanana, Midjourney, Seedance, and local ComfyUI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jau123](https://clawhub.ai/user/jau123)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and developers use this skill to generate images or videos, enhance prompts, search curated prompt examples, configure generation providers, and manage local ComfyUI workflows through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a pinned npm MCP server and can use provider credentials.

Mitigation: Install only when comfortable running the pinned package and provide credentials only for providers you intend to use.

Risk: Prompts, provider credentials, and explicitly selected reference images may be sent to the configured generation provider or upload gateway.

Mitigation: Avoid private reference images unless that processing is acceptable; prefer local ComfyUI for more local-only workflows.

## Reference(s):

- [Provider Comparison & Configuration](references/providers.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub Skill Page](https://clawhub.ai/jau123/skills/creative-toolkit)
- [MeiGen Model Comparison](https://www.meigen.ai/model-comparison)
- [meigen npm package](https://www.npmjs.com/package/meigen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompts, provider setup guidance, MCP tool calls, generation status IDs, output URLs, saved file paths, and troubleshooting steps.]

## Skill Version(s):

1.0.37 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
