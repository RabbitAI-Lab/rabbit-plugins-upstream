## Description:

Uses Grok 4.2 through dLazy's hosted service for text generation, conversational answers, and reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke the dLazy CLI to generate text, answer questions, and assist with reasoning through Grok 4.2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or local files supplied to the CLI may be sent to dLazy's hosted services.

Mitigation: Do not submit sensitive prompts or files unless sharing them with dLazy is acceptable.

Risk: Installing the third-party CLI or saving an API key locally introduces package and credential exposure.

Mitigation: Review the pinned @dlazy/cli package before use; consider on-demand npx execution and DLAZY_API_KEY instead of persisted credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI homepage (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (declared in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text returned in a CLI JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task identifier before results are available.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
