## Description:

This skill guides agents to generate high-contrast, resonant, story-driven short-video spoken scripts using a seven-step structure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to draft short-video spoken scripts, character story shares, and personal IP viewpoint scripts with a structured narrative arc. The artifact also includes dLazy CLI image-generation guidance, so users should install it only when they intend to use that external workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as a spoken-script helper but can steer the agent into dLazy CLI image generation, terminal commands, and external API use.

Mitigation: Install and invoke it only when the user intentionally wants the dLazy workflow, and review proposed commands before execution.

Risk: Using the dLazy CLI may require a dLazy account or API key and may store credentials in local CLI configuration.

Mitigation: Use a dedicated, revocable API key, protect the local configuration file, and rotate or revoke the key when access is no longer needed.

Risk: Prompts, parameters, and local media paths may be sent to dLazy services or uploaded to dLazy-hosted storage when the workflow is used.

Mitigation: Do not provide sensitive prompts or media unless external processing is acceptable, and confirm each local file path before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown or plain text script content with optional bash command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a seven-step spoken-script structure; may call the dLazy CLI for external image generation after user confirmation.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
