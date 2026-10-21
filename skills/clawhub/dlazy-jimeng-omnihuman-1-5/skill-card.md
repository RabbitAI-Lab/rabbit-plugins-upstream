## Description:

Generate digital-human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request digital-human broadcast videos from a portrait and an audio clip or text prompt through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected portrait or audio files are sent to a third-party cloud service, which hosts generated assets.

Mitigation: Review the dLazy service and avoid sending sensitive media without authorization.

Risk: Login may store an API key in local CLI configuration.

Mitigation: Protect the local account and rotate or revoke the key if needed.

Risk: Installing the third-party CLI globally persists a local executable.

Mitigation: Review the dLazy CLI source and use the pinned npx option if a global install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source (skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON responses]

**Output Format:** [Markdown guidance and commands; the CLI returns JSON with generated asset URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are hosted by dLazy; the CLI can download a result locally on request.]

## Skill Version(s):

1.3.31 (source: ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
