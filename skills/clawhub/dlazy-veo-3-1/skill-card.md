## Description:

Generates cinematic videos from text or image inputs using Google Veo 3.1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from prompts and images, or extend existing video, via the dLazy Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's cloud service.

Mitigation: Only submit prompts and files intended for upload.

Risk: The CLI can save an API key under the user's profile.

Mitigation: Protect the local key and use the pinned npx invocation if a persistent global CLI is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results include hosted media URLs or an asynchronous task ID; generated media can be saved locally.]

## Skill Version(s):

1.3.22 (source: ClawHub release; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
