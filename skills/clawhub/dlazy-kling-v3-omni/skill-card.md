## Description:

Uses dLazy's Kling V3 Omni workflow to generate dynamic videos from text prompts and supported image or video references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request video generation from an agent through the dLazy CLI. It supports prompt-based generation with optional image or video references and can return generated asset URLs or save outputs locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads prompts and user-provided media to dLazy-hosted services for generation.

Mitigation: Only pass media and prompt content that is appropriate to share with dLazy, and review the service terms before use.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party CLI package and hosted API endpoints.

Mitigation: Install the pinned CLI version from the declared source only after reviewing the linked source or npm package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI may return generated file URLs, async task identifiers, or locally saved assets.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
