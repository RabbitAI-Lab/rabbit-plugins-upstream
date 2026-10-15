## Description:

Helps agents generate short videos with MiniMax H3 from text prompts, keyframes, or reference media through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text, first and last frames, or reference images, videos, and audio via dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any selected local media are sent to dLazy's hosted service.

Mitigation: Review prompts and media before submitting them; use the third-party service only when appropriate for the content.

Risk: The dLazy CLI saves an API key locally for authenticated requests.

Mitigation: Keep the key private and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include hosted asset URLs or an asynchronous task ID; a save option can download the asset.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
