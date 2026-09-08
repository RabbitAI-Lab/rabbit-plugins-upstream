## Description:

Studies a user-provided reference image or video, then recreates the same look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run the dLazy video-image-replicate template for reference-based image or video recreation through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached local files are sent to dLazy hosted services.

Mitigation: Use the skill only with data that may be shared with dLazy, and review dLazy service terms before sending sensitive media or prompts.

Risk: Installing and running the dLazy npm CLI requires API-key handling and introduces normal package supply-chain exposure.

Mitigation: Prefer the pinned npx invocation when avoiding a global install, review the CLI source or package before use, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline bash code blocks and streamed CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded files or generated media returned by the dLazy hosted service.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
