## Description:

Replicates a user-provided reference image or video by recreating its look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy video-image-replicate hosted agent from a CLI. It helps them provide prompts and optional reference media so the service can recreate an image or video style with their own subject, product, or characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference media, attached files, and project context are sent to and may be retained by dLazy.

Mitigation: Use the skill only with assets appropriate for dLazy processing; avoid sensitive or rights-restricted media and clear project sessions when needed.

Risk: A saved dLazy API key can continue authorizing requests if left in local configuration after use.

Mitigation: Use npx for one-off sessions when practical and rotate or revoke the dLazy API key if you stop using the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline bash commands and CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links or references to generated image or video assets returned by dLazy.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
