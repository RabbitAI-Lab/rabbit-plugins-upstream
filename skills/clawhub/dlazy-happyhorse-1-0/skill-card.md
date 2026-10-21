## Description:

Guides agents in generating or editing videos with Happy Horse 1.0 using text prompts, first frames, reference images, or existing video through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate videos from text or images, or edit existing video, through dLazy's Happy Horse 1.0 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are uploaded to dLazy for generation.

Mitigation: Review dLazy's service terms and avoid submitting sensitive prompts or media without authorization.

Risk: CLI installation runs a third-party npm package, and login or saved-key authentication persists an API key locally.

Mitigation: Review and trust the CLI package before installation; use per-invocation DLAZY_API_KEY or npx if less local persistence is preferred.

## Reference(s):

- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns media URLs in JSON; the CLI can optionally download generated assets.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
