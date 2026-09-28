## Description:

Guides agents in composing MeiGen image and video generation, product-image tools, and optional creative planning within an existing workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jau123](https://clawhub.ai/user/jau123)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through authorized image and video generation, product imagery, background removal, and upscaling while retaining control of prompts, scope, and spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, references, job metadata, and uploaded images may reach MeiGen or configured providers; prepared references may have shareable URLs.

Mitigation: Avoid submitting sensitive material and treat prepared reference URLs as shareable.

Risk: Generation can spend purchased credits or incur provider charges.

Mitigation: Check current prices and confirm the requested scope and budget before spending or accepting a price change.

Risk: Credentials or the installed package may be exposed or differ from the reviewed skill release.

Mitigation: Keep API keys in private host settings or environment variables and inspect the actual npm package version if supply-chain assurance is needed.

## Reference(s):

- [MeiGen skill release on ClawHub](https://clawhub.ai/jau123/skills/creative-toolkit)
- [MeiGen skill homepage listed in the skill](https://github.com/jau123/MeiGen-AI-Design-MCP)
- [Provider configuration](references/providers.md)
- [Troubleshooting and data handling](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with tool calls, status, and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task handles, generated media URLs, and local paths when available.]

## Skill Version(s):

2.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
