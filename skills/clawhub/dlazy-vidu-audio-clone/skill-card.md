## Description:

Clone a voice from reference audio and generate new text reading audio using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI for Vidu voice cloning, providing reference audio and prompt text to generate cloned-voice speech through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference audio, and local media paths provided to the CLI are sent to dLazy's hosted API and media storage.

Mitigation: Only pass audio and prompt content that is appropriate for dLazy's hosted service, and confirm the user intends to use dLazy/Vidu before invoking the skill.

Risk: Global CLI installation and persistent local API-key configuration can increase supply-chain and credential persistence exposure.

Mitigation: Prefer npx or an isolated environment when appropriate, review the linked CLI source or package for supply-chain concerns, and use a revocable key or DLAZY_API_KEY for non-persistent authentication.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return synchronous JSON with hosted output URLs or asynchronous task identifiers for later polling.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
