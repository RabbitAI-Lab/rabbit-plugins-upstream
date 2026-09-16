## Description:

Generate coherent transition videos from first and last frame images using Jimeng's first-tail frame video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI/API for Jimeng first-tail frame video generation from a prompt plus first-frame and last-frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm package and hosted dLazy API for execution.

Mitigation: Prefer the pinned npx/on-demand invocation, review the linked CLI source or npm package before use, and install only in environments where that third-party dependency is acceptable.

Risk: Prompts, selected media files, and the dLazy API key may be sent to dLazy services during normal use.

Mitigation: Avoid submitting sensitive media or prompts unless permitted, store the API key according to local credential policy, and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with bash commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs, saved local files when --save is used, or async task status when --no-wait is used.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
