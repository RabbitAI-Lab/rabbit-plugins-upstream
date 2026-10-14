## Description:

Helps agents turn a static character image into an action video with Jimeng Dream Actor through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating action videos from character images and text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be uploaded to dLazy's hosted service.

Mitigation: Confirm the exact media files and prompt before generation; avoid sending sensitive content.

Risk: Generation can consume paid API credits.

Mitigation: Review the cost estimate with --dry-run before submitting a paid request.

Risk: Login may store an API key locally, and a global CLI installation persists.

Mitigation: Protect the local API key and use the pinned npx command if a persistent global installation is unwanted.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns generated-media URLs; results may also be saved locally.]

## Skill Version(s):

1.3.29 (source: ClawHub release; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
