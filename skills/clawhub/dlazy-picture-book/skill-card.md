## Description:

Creates a complete picture book from a theme by drafting paged story text, generating style-consistent illustrations and background music through dLazy services, and assembling a self-contained HTML book.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create bilingual picture books, storybooks, children's books, illustrated stories, and bedtime stories from a theme. The agent coordinates story writing, image and music generation through dLazy services, and local HTML assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generated media requests, and uploaded reference images are processed by dLazy cloud services.

Mitigation: Use the skill only when this cloud processing is acceptable, avoid sensitive inputs unless approved, and review dLazy service terms and the @dlazy/cli package before use.

Risk: The skill stores a dLazy API key in local CLI configuration or accepts it through DLAZY_API_KEY.

Mitigation: Protect the local configuration file, prefer per-invocation environment variables when appropriate, and rotate or revoke the key if exposure is suspected.

Risk: Global installation of @dlazy/cli leaves persistent tooling on the machine.

Mitigation: Use npx @dlazy/cli@1.2.3 when a temporary invocation is preferred, and review the package before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-picture-book)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown guidance with bash commands and JSON examples; generated artifacts include book.json, image files, music files, and a self-contained index.html.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, python3, curl, the dLazy CLI, and a dLazy API key; generated images and music are downloaded into relative paths for portable offline viewing.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
