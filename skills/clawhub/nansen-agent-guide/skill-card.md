## Description:

Guides agents on when to use Nansen's AI research agent versus direct CLI data commands for crypto research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and crypto researchers use this guide to choose between Nansen AI analysis and structured CLI data requests, while respecting account authentication and credit costs.

### Deployment Geography for Use:

Global, subject to Nansen's geographic and sanctions checks.

## Known Risks and Mitigations:

Risk: Agent research queries can consume substantial account credits, especially in expert mode.

Mitigation: Review CLI costs and account permissions; use direct data commands for simple requests and monitor credit-consuming calls.

Risk: Nansen account sessions and API keys permit account-level API requests.

Mitigation: Use only authorized credentials, check authentication status, and stop on authentication failures rather than switching to another account or payment method.

## Reference(s):

- [Nansen Agent Guide on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-agent-guide)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Nansen CLI and an authorized Nansen account or API key; research calls may consume credits.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
