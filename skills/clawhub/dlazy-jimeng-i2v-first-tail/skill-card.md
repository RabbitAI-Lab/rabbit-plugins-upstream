## Description:

Generate coherent transition videos using Jimeng's first and tail frame models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Jimeng first-frame and last-frame image-to-video generation. It supports authenticated cloud generation using a prompt, first frame, last frame, and duration parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input media are sent to dLazy's hosted service for generation.

Mitigation: Confirm that the user is comfortable sending the selected prompt and media to dLazy before invoking the command.

Risk: Generated outputs are hosted by dLazy and returned as service URLs.

Mitigation: Avoid submitting sensitive media unless the user's data handling requirements permit hosted output storage.

Risk: Logging in can store a dLazy API key in local CLI configuration for later use.

Mitigation: Use per-invocation credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted output URLs; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
