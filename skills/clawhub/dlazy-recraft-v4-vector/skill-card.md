## Description:

Text-to-vector model that outputs SVG results, suitable for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, designers, and developers use this skill to ask an agent to invoke dLazy's Recraft V4 Vector model for logo, icon, and scalable asset generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files supplied to the skill are sent to dLazy's cloud API and media storage.

Mitigation: Use the skill only for prompts and files that are appropriate for dLazy's hosted service.

Risk: The security summary notes a mismatch between SVG/vector claims and PNG examples.

Mitigation: Verify returned mimeType and file extension before treating outputs as SVG vectors.

Risk: The CLI stores or accepts a dLazy API key for authenticated requests.

Mitigation: Protect the local config file, prefer per-invocation keys where appropriate, and rotate or revoke keys if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown instructions with CLI commands, JSON command output, and generated asset URLs or downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports async generation and optional local save paths.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
