## Description:

Compose MeiGen image/video and five dedicated image tools inside an existing workflow, or opt into creative planning. Preserves caller prompts, parameters, approved count and budget; includes discovery and recoverable task handles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jau123](https://clawhub.ai/user/jau123)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent workflow to MeiGen image and video generation, dedicated visual workflows, prompt enhancement, provider selection, billing checks, and recoverable task status handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a pinned third-party npm MCP server with access to credentials, local files explicitly provided by the user, and network routes configured for generation.

Mitigation: Install only in environments where that access is acceptable, keep API keys in private host settings, and review the package or source before use in sensitive deployments.

Risk: Cloud generation routes can send prompts, references, image URLs, and job metadata to MeiGen and configured providers.

Mitigation: Avoid submitting confidential material unless the configured services are approved for it, and treat generated upload URLs as shareable links.

Risk: Paid generation and dedicated visual workflows can consume purchased credits or provider billing when submitted.

Mitigation: Use live pricing checks, pass confirmed credit amounts within the accepted budget, and require explicit acceptance for price changes or downscale tradeoffs.

## Reference(s):

- [Creative Toolkit on ClawHub](https://clawhub.ai/jau123/skills/creative-toolkit)
- [Providers and configuration](references/providers.md)
- [Troubleshooting](references/troubleshooting.md)
- [MeiGen API keys](https://www.meigen.ai/profile/api-keys)
- [MeiGen model comparison](https://www.meigen.ai/model-comparison)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return tool handles, status details, generated URLs, saved paths, and billing or retry guidance from invoked MCP tools.]

## Skill Version(s):

1.0.38 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
