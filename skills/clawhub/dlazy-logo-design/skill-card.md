## Description:

logo design, logo maker, make a logo, brand identity, brand kit, VI design — brand-gene analysis, strategy, concepts, refinement, multi-context delivery, evaluation. Use to create, upgrade, or evaluate a logo / brand mark; ships a transparent-background logo with a live multi-context preview.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, upgrade, or evaluate logo and brand identity assets through dLazy's logo-design template, including transparent-background logo output and multi-context previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party hosted dLazy service for logo-design requests.

Mitigation: Install and use it only when the user is comfortable sending prompts and selected inputs to dLazy's service.

Risk: Attached local reference files are uploaded to dLazy storage before use.

Mitigation: Do not attach private or sensitive reference files unless the user is willing to upload them to dLazy storage.

Risk: The dLazy API key can be stored in local CLI configuration.

Mitigation: Use OS-user-restricted configuration, or rotate or revoke the API key from the dLazy dashboard when access should be removed.

Risk: A persistent global CLI install changes the user's environment.

Mitigation: Use the pinned npx invocation when the user does not want a persistent global CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-design)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and terminal text with inline shell commands and generated design assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded user files and generated logo assets from the dLazy hosted service.]

## Skill Version(s):

1.3.6 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
