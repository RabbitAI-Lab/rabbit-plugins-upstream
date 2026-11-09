## Description:

Moonshot AI thinking model with text, image, and video understanding. Suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill through the dLazy CLI for complex text analysis, coding, and writing, with image and video understanding. It returns Kimi K3 model responses to the supplied prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan could not establish how the CLI handles credentials, and login requires a dLazy API key.

Mitigation: Review the dLazy CLI and authentication flow before signing in; avoid sharing credentials or sensitive prompts until you trust the service and its key handling.

Risk: Prompts and supplied local media are sent to dLazy's hosted service for processing.

Mitigation: Review the service terms and avoid submitting sensitive prompts or files unless their cloud processing is appropriate.

## Reference(s):

- [dLazy CLI project homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Generated asset links]

**Output Format:** [Model responses returned as text or JSON, with generated asset URLs when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a generation ID for later polling.]

## Skill Version(s):

1.2.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
