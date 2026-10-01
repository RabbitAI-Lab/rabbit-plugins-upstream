## Description:

Generates text, answers questions, and supports reasoning with Grok 4.2 through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke the skill for text generation, conversational answers, and reasoning with Grok 4.2. Requests are sent to dLazy's hosted service and require a dLazy API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat-style triggers may send ordinary prompts to a third-party hosted service unexpectedly.

Mitigation: Invoke explicitly when dLazy processing is intended and avoid including confidential information in prompts.

Risk: Supported local media or file paths may be uploaded, and the documentation is unclear about file inputs and outputs.

Mitigation: Check the requested inputs before invoking and avoid sensitive file paths unless their upload is intended.

Risk: Installing the external CLI grants its package execution on the local system.

Mitigation: Review the npm package before global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text returned through a CLI JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may initially return a task ID; the documented output example shows an image despite the text-generation description.]

## Skill Version(s):

1.3.22 (source: ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
