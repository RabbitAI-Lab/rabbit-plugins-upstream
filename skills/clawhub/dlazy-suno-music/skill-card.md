## Description:

Generates Suno music from prompts in inspiration or custom mode, with support for vocal and instrumental tracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent configure and invoke the dLazy CLI for Suno music generation, including prompt, style, vocal, asynchronous, and save options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and dLazy account credentials.

Mitigation: Install only if you trust dLazy, prefer npx or an isolated environment, and rotate or revoke the dLazy API key if compromise is suspected.

Risk: Prompts and referenced media files are sent to dLazy cloud services for generation.

Mitigation: Avoid passing unrelated or sensitive local files and review dLazy service terms before using confidential inputs.

Risk: Generated result URLs and optional downloads may be stored outside the local workspace.

Mitigation: Review returned URLs and saved files before reuse, sharing, or publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated music is returned through hosted result URLs and can be downloaded with the CLI save option.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
