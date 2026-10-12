## Description:

Guides agents in generating digital-human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide agents in producing digital-human broadcast videos from a portrait and audio or text through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portraits, audio, and prompts sent for generation are processed by dLazy's hosted service.

Mitigation: Only submit media and prompts you intend to share with the service.

Risk: Signing in may save an API key on the user's device.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if exposed.

Risk: Installing a third-party CLI requires trust in its package and dependencies.

Mitigation: Review the linked CLI source before installation and prefer the pinned npx command for one-time use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source (skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses may include hosted result URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.27 (source: ClawHub release evidence; bundled skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
