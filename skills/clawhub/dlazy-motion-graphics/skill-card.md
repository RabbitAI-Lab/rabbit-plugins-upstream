## Description:

Creates code-driven motion graphics, kinetic typography, animated text videos, animated infographics, and explainer animations using Remotion code rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and developers use this skill to create and iterate on project-scoped motion graphics, animated typography, infographics, and explainer videos through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files may be sent to dLazy services for hosted generation.

Mitigation: Use only data approved for dLazy processing and attach files only when you are comfortable uploading them to dLazy storage.

Risk: The skill depends on the npm-distributed dLazy CLI, which can be installed globally.

Mitigation: Review the linked CLI source or use the pinned npx form, npx @dlazy/cli@1.2.3, to avoid keeping a persistent global binary.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Protect the local config and environment, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped dLazy chat output; attached local files are uploaded to dLazy storage before use.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
