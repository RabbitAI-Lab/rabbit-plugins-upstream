## Description:

Converts static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Jimeng Dream Actor image-to-video generation from a prompt and one reference image or video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to the dLazy hosted API and media storage.

Mitigation: Pass only media needed for the current task and avoid sending sensitive content unless the user accepts the third-party cloud processing risk.

Risk: The dLazy API key is stored in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Use a revocable API key, prefer per-run DLAZY_API_KEY for sensitive environments, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill runs a third-party npm CLI, with optional global installation.

Mitigation: Prefer npx or a local install over a global install, keep the pinned package version, review the package source before use, and avoid administrator privileges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown instructions with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated media URLs from files.dlazy.com and can save the result asset to a local path when --save is used.]

## Skill Version(s):

1.3.15 (source: evidence.release.version; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
