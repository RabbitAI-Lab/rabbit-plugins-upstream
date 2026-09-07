## Description:

Generate high-quality images with Vidu Q2 from text prompts or reference images through the pinned dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Vidu Q2 through dLazy's hosted service. It is suited for workflows that can send prompts, generation parameters, and selected media files to dLazy for image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted API and media storage.

Mitigation: Avoid passing private files unless upload is intended, and use dry-run mode when checking payloads or estimated cost.

Risk: The skill depends on a pinned third-party npm CLI that handles authentication and API calls.

Mitigation: Use the pinned version declared by the artifact, prefer npx for on-demand execution when a global install is not desired, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses containing generated image metadata and hosted file URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers; generated assets may be downloaded locally when a save path is provided.]

## Skill Version(s):

1.3.13 (source: ClawHub release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
