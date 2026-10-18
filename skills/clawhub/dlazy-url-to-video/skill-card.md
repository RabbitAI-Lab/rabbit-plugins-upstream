## Description:

Turns a webpage URL into a promotional, advertising, or demo video through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a webpage link into a promotional video, social ad, or product demo with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to an external service, and attached files are uploaded when used.

Mitigation: Share only content approved for dLazy processing; review attachments before sending them.

Risk: The CLI can store an API key locally.

Mitigation: Use the environment variable option when local key storage is unsuitable.

Risk: Installing the CLI adds an external npm package to the environment.

Mitigation: Review the pinned package and its linked source before global installation in sensitive environments.

## Reference(s):

- [dLazy CLI (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown with links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is handled by the external dLazy service.]

## Skill Version(s):

1.0.26 (source: ClawHub release metadata; skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
