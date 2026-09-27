## Description:

Generate dynamic videos from a single first-frame image and prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Jimeng image-to-video service, providing a first-frame image and prompt to generate a short video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths may be sent to dLazy cloud endpoints, and local files passed as media inputs may be uploaded to files.dlazy.com.

Mitigation: Use the skill only with content approved for third-party cloud processing and avoid passing sensitive files or prompts unless dLazy is approved for that data.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation credentials or protect and rotate the saved API key according to local credential-handling policy.

Risk: The artifact has inconsistent first-frame option examples, which may cause failed or unintended calls.

Mitigation: Check `dlazy jimeng-i2v-first -h` and use the documented first-frame flag before running a generation request.

## Reference(s):

- [Skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying service can return hosted media URLs or an asynchronous task identifier.]

## Skill Version(s):

1.3.20 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
