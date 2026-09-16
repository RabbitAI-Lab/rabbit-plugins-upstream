## Description:

MiniMax Hailuo omni-modal video generation skill for creating 5-15 second clips with native stereo audio from text prompts, frame transitions, or multi-asset references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy CLI for MiniMax Hailuo video generation, including text-to-video, first/last-frame transitions, and generation from image, video, or audio references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm CLI.

Mitigation: Review the linked dLazy CLI source or npm package before installing, prefer npx or an isolated environment when avoiding a global binary, and do not run it as root or administrator.

Risk: The CLI may store a dLazy API key in the local user configuration.

Mitigation: Use a revocable dLazy API key, keep it scoped to the intended organization, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Prompts and referenced media files are uploaded to dLazy services for generation.

Mitigation: Only submit prompts and media files that are appropriate to share with the dLazy hosted service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects containing generated media URLs; optional local media files when saved by the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Synchronous runs return generated output URLs; asynchronous runs may return a generateId for later polling.]

## Skill Version(s):

1.2.13 (source: ClawHub release evidence; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
