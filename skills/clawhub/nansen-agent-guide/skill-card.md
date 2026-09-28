## Description:

Guides agents in choosing Nansen AI research or direct CLI data commands to answer research questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Nansen users use this guide to choose between interpreted research with the Nansen agent and structured data retrieval with direct CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nansen agent and data calls may consume account credits.

Mitigation: Check account billing and use direct data commands for simple queries before making paid calls.

Risk: An API key or browser session may select the wrong account or fail to authenticate.

Mitigation: Confirm the selected account and browser-session behavior; stop on invalid authentication rather than switching to anonymous payment.

## Reference(s):

- [Nansen Agent Guide on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-agent-guide)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes research and data requests; Nansen calls require account authentication and may consume credits.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
