## Description:

Generate dynamic videos from a single first-frame image and prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Jimeng image-to-video results by supplying a first-frame image, prompt, duration, and optional save or asynchronous execution settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill's required external npm CLI may execute code that is not bundled with the skill artifact.

Mitigation: Review or sandbox @dlazy/cli@1.2.3 before installing and prefer npx or another isolated execution method over a global install.

Risk: The skill handles dLazy API keys and stores or accepts credentials through the local CLI configuration or environment variables.

Mitigation: Only provide API keys intended for dLazy use and rotate or revoke the key when it is no longer needed.

Risk: Prompts and local media files supplied to the command are sent to dLazy's hosted API and media storage.

Mitigation: Only submit media files and prompts that are appropriate to send to dLazy's hosted service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated media URLs, optional downloaded files, and Markdown guidance for command use and error handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates, asynchronous task IDs, polling guidance, timeout configuration, and optional local save paths.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
