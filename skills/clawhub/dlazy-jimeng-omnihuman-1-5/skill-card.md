## Description:

Generates realistic digital-human broadcast videos from a portrait image and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to have an agent invoke the dLazy CLI for creating digital-human broadcast videos from supplied portrait images and audio or text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portrait images, audio, and prompts may be uploaded to dLazy services for generation.

Mitigation: Use only media and prompts approved for third-party SaaS processing, and avoid submitting confidential or regulated content unless the account terms allow it.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Protect the user configuration file, prefer per-invocation environment variables when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Installing a global CLI adds normal package supply-chain exposure.

Mitigation: Use the pinned npx invocation or a contained install when possible, and review the declared source and npm package before installation.

Risk: Generation calls may consume dLazy account credits.

Mitigation: Use dry-run or cost-estimate behavior where available before submitting expensive jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dLazy CLI source link declared in metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs, asynchronous task IDs, or saved generated video assets when a save path is provided.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
