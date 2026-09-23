## Description:

Generates coherent transition videos from provided first-frame and last-frame images using Jimeng's first-tail video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate transition videos by supplying a prompt plus first-frame and last-frame images to the dLazy Jimeng CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media files are sent to dLazy's hosted API and media storage.

Mitigation: Use only media and prompt content approved for processing by dLazy, and review dLazy service terms before use.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke saved keys when access should change.

Risk: Installing a third-party CLI introduces package trust and supply-chain risk.

Mitigation: Use the pinned @dlazy/cli version, prefer npx for ephemeral use, and confirm the package is trusted before installation.

Risk: The artifact examples appear inconsistent with the documented firstFrame and lastFrame options.

Mitigation: Run dlazy jimeng-i2v-first-tail -h and use the documented firstFrame and lastFrame flags before submitting jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted result URLs or optional saved files; asynchronous calls may return a task identifier for polling.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
