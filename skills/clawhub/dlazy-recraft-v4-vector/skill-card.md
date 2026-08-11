## Description:

Text-to-vector model that outputs SVG results for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate vector-style design assets from text prompts through the dLazy hosted Recraft V4 Vector service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any referenced media are sent to dLazy's hosted service for generation.

Mitigation: Avoid submitting sensitive content unless the user accepts that cloud processing path.

Risk: The skill can rely on a locally stored dLazy API key.

Mitigation: Use per-run DLAZY_API_KEY where appropriate, rotate keys from the dLazy dashboard, and check permissions on ~/.dlazy/config.json on shared machines.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Prefer the pinned npx invocation when a persistent global install is not needed.

Risk: Security evidence notes that users should verify the actual output format.

Mitigation: Inspect returned assets before treating them as true SVG or production-ready vector files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs return generated output metadata and hosted result URLs; asynchronous runs can return a generateId for polling.]

## Skill Version(s):

1.3.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
