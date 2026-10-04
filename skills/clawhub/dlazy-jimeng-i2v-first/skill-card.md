## Description:

Helps agents generate short Jimeng videos from a first-frame image and a text prompt through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to guide an agent in generating short videos from a supplied first-frame image and prompt using dLazy's hosted Jimeng service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dLazy API key is required and may be stored locally.

Mitigation: Protect the local configuration or supply the key per invocation; rotate or revoke it if exposed.

Risk: Selected images and prompts are sent to dLazy's hosted service.

Mitigation: Only submit material approved for upload to a third-party service.

Risk: Generation may incur charges and saving a result may overwrite a local file.

Mitigation: Use --dry-run to estimate cost and check the --save destination before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and examples of JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can return a hosted output URL or an asynchronous task ID; an optional save path downloads the result locally.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
