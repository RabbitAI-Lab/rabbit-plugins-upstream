## Description:

Helps agents generate PixVerse C1 videos from text prompts, images, first and last frames, or reference images through dLazy's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short AI-generated videos from text or visual references and retrieve the resulting media through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy's cloud service.

Mitigation: Send only prompts and files approved for third-party processing.

Risk: The third-party CLI can save an API key locally.

Mitigation: Prefer the pinned on-demand CLI if a global install is unnecessary; rotate or revoke the key when you stop using the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns generated media URLs; asynchronous requests return a task ID for follow-up.]

## Skill Version(s):

1.2.31 (source: ClawHub release metadata; bundled skill frontmatter says 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
