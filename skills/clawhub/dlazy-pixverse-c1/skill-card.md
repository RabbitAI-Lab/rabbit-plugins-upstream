## Description:

Helps agents generate PixVerse C1 videos from text, images, first and last frames, or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request PixVerse C1 video generation from text prompts and optional image references, then retrieve the generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the third-party CLI introduces software outside the skill files.

Mitigation: Review the package before installation and use the pinned npx command if a persistent global install is unnecessary.

Risk: Logging in or setting an API key stores a dLazy credential locally.

Mitigation: Protect access to the local credential and rotate or revoke it if exposed.

Risk: Prompts and explicitly supplied media are sent to dLazy-hosted services.

Mitigation: Avoid sending private prompts or media unless sharing them with the service is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands and generated-media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with media URLs or asynchronous task IDs; results can optionally be downloaded.]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata; bundled skill frontmatter says 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
