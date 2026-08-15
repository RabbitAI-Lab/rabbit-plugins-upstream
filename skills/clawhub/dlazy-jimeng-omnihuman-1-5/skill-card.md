## Description:

Generate realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create digital-human broadcast videos from portrait images plus audio or text prompts through dLazy's Jimeng OmniHuman 1.5 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and portrait or audio files are sent to dLazy hosted endpoints for generation.

Mitigation: Invoke the skill only for explicit Jimeng OmniHuman or dLazy requests, and avoid sending sensitive media unless the user accepts hosted processing.

Risk: Logging in with the CLI stores an API key in the local dLazy configuration file.

Mitigation: Use DLAZY_API_KEY or the pinned npx invocation when minimizing local persistence, and rotate or revoke organization keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON with generated media URLs and CLI status fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID when --no-wait is used; generated media URLs are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.6 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
