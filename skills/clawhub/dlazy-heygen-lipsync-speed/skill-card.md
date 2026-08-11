## Description:

HeyGen Lipsync Speed generates fast lip-sync outputs through the dLazy hosted API for scenarios that need rapid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to invoke dLazy's HeyGen Lipsync Speed model for quick lip-sync generation from video and audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video or audio paths supplied to the skill can be uploaded to dLazy servers, and generated outputs are hosted remotely.

Mitigation: Use approved media only, avoid sensitive or restricted content, and confirm the remote hosting behavior is acceptable before invoking the skill.

Risk: The dLazy API key may be saved in the local CLI configuration on the user's machine.

Mitigation: Prefer per-invocation credentials or `npx @dlazy/cli@1.2.3` on shared machines, and rotate or revoke the key if local storage may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include generated media URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
