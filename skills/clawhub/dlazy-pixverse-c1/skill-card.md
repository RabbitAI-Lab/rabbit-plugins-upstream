## Description:

Helps agents generate PixVerse C1 videos from text prompts, images, reference images, or first and last frames using the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short PixVerse C1 videos from text prompts and optional image inputs, then retrieve the generated result or an asynchronous task ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Submit only prompts and media you are comfortable sharing with dLazy.

Risk: Logging in stores a dLazy API key locally.

Mitigation: Protect the local CLI configuration, or provide the key per invocation through DLAZY_API_KEY.

Risk: The skill depends on a third-party npm CLI package.

Mitigation: Review the pinned package and its source before installation when stronger supply-chain assurance is needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON result or video URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID to check later.]

## Skill Version(s):

1.2.23 (source: ClawHub release evidence; bundled skill frontmatter says 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
