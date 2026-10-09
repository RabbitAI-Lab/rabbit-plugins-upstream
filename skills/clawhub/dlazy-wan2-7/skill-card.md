## Description:

Helps agents generate videos from text prompts, first and last frames, or reference media using Tongyi Wanxiang 2.7 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request videos from text, reference media, or first and last frames via a dLazy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party npm CLI runs code outside the skill files.

Mitigation: Review the CLI source before installation and use the pinned npx command if a persistent global installation is unnecessary.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Protect the local configuration and rotate or remove the key when it is no longer needed.

Risk: User-selected local media is uploaded to dLazy for generation.

Mitigation: Submit only media you are comfortable sharing with dLazy.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with CLI commands and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an asynchronous task ID or a link to generated media; results can optionally be downloaded.]

## Skill Version(s):

1.3.25 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
