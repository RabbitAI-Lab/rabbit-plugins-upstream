## Description:

Analyzes Nansen smart-money flows, holdings, and trades to assess whether investors are entering, accumulating, reducing, or exiting a token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Token researchers and analysts use this skill to compare short- and long-term smart-money activity and identify whether notable holders are still buying.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls, especially in loops, may consume credits or spend wallet funds under existing payment limits.

Mitigation: Use a deliberately selected API key or browser session, confirm the CLI package is trusted, and monitor the number and cost of calls.

Risk: An unverified or failed authentication state could lead to unintended access attempts.

Mitigation: Check authentication status before research and stop on failed authentication or uncertain session renewal; do not switch to anonymous access to retry.

## Reference(s):

- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)
- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-smart-money-trend)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interprets Nansen CLI research results for a selected token and chain.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
