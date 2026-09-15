## Description:

Text-to-vector generation wrapper for Recraft V4 Vector, suitable for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external agents use this skill to call dLazy's Recraft V4 Vector command from a prompt and generate logo, icon, or scalable design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI sends prompts and selected local files to hosted dLazy endpoints.

Mitigation: Use only prompts and files approved for dLazy processing, and avoid passing unrelated private files or secrets.

Risk: The skill requires a dLazy API key and can store it in local CLI configuration.

Mitigation: Prefer least-privilege key handling where available, protect the local config file, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: The skill relies on an external npm CLI package.

Mitigation: Prefer the pinned npx invocation or an isolated install, and review the linked source or package before use.

Risk: The documentation conflicts on whether the generated asset is SVG/vector or PNG.

Mitigation: Check the returned MIME type and saved file before using the result in SVG- or vector-specific workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted URLs or saved files; async mode can return a task identifier for polling.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter is 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
