## Description:

Generates text, answers questions, and supports reasoning through the dLazy-hosted Grok 4.2 workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users use this skill to draft text, ask questions, and request reasoning through the dLazy CLI with their own API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected files are sent to dLazy's hosted service.

Mitigation: Invoke only when you intend to share that content; review the service terms first.

Risk: Installing the third-party CLI runs external software.

Mitigation: Review the package before installation and use the pinned npx invocation if a persistent global binary is unnecessary.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text returned through a CLI JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task ID when invoked with --no-wait.]

## Skill Version(s):

1.3.23 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
