## Description:

Generates digital-human presenter videos from a portrait image and audio or text using Jimeng OmniHuman 1.5 through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request digital-human presenter videos from portrait images with audio or text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, audio, prompts, and related parameters are sent to dLazy's hosted service.

Mitigation: Submit only content approved for third-party processing.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: Installing the external CLI globally keeps it on the system.

Mitigation: Prefer the documented pinned npx invocation if a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions and CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain a hosted media URL or an asynchronous task ID.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; bundled frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
