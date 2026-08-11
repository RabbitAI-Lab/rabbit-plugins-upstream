## Description:

URL to Video turns a pasted webpage URL into a promotional, social ad, or product demo video through dLazy's hosted website-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to start or continue dLazy website-to-video projects from a URL, with optional attached reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, URLs, and chosen attachments are sent to dLazy's hosted service.

Mitigation: Install and invoke only when the user is comfortable sharing the relevant prompt, URL, and attachments with dLazy.

Risk: Broad trigger phrases could invoke video generation on a pasted link or generic marketing request without clear intent.

Mitigation: Confirm explicit video-generation intent before invoking the skill.

Risk: The dLazy API key is saved locally for CLI use.

Mitigation: Revoke or rotate the saved dLazy API key when access should be removed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and CLI output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned dLazy CLI package and may send prompts, URLs, and selected attachments to dLazy's hosted service.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
