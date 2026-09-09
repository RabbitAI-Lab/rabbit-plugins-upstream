## Description:

Use when installing the full Pruna generative media suite: guides, tools, and workflows in one package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative media builders use this skill to install and navigate the full Pruna suite for image, video, audio, and multi-step generative media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install command uses npx to fetch and run the current skills CLI.

Mitigation: Verify trust in the pruna-ai publisher profile and the PrunaAI/pruna-skills source before installation.

Risk: Media workflows may require PRUNA_API_KEY or REPLICATE_API_TOKEN and can upload inputs or incur provider costs.

Mitigation: Provide credentials only for intended external API calls and review provider usage before running generation workflows.

## Reference(s):

- [Pruna dashboard](https://dashboard.pruna.ai/)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and installation tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes install commands, reading order, credential requirements, and tool or workflow selection guidance.]

## Skill Version(s):

1.0.11 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
