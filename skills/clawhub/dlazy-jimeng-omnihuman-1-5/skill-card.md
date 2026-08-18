## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Jimeng OmniHuman 1.5 workflow for generating digital human broadcast videos from a portrait image plus audio or text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied image or audio files are sent to dLazy for cloud inference, and generated outputs are hosted by dLazy.

Mitigation: Use the skill only with content the user is permitted to upload to dLazy, and avoid submitting sensitive or regulated material unless the user's dLazy terms and controls support that use.

Risk: The dLazy login flow can save an API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for non-persistent authentication when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: A global CLI install persists the dLazy binary on the system.

Mitigation: Prefer the pinned npx invocation for one-off use when the user does not want a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as dLazy-hosted output URLs; asynchronous runs may return a task identifier for later polling.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
