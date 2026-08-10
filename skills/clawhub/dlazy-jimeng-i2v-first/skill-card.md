## Description:

Generate dynamic videos based on a single first-frame image and prompts using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short Jimeng image-to-video outputs from a first-frame image, prompt, and duration through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy-hosted services for generation.

Mitigation: Use the skill only with media and prompts that are appropriate to send to dLazy, and avoid submitting sensitive or regulated content unless that use is approved.

Risk: The dLazy API key may be persisted in ~/.dlazy/config.json, and the reviewed CLI package does not enforce the user-only file permissions claimed by the skill.

Mitigation: Prefer DLAZY_API_KEY per invocation, verify local config permissions before persistent use, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command examples; the invoked CLI returns JSON result data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow accepts a prompt, first-frame image path or URL, duration, dry-run, async, and timeout options.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
