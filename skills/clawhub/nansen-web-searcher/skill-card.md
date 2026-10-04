## Description:

Search the web for one or more queries in parallel to find current information, news, prices, and web content alongside on-chain Nansen data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can search for current web information to complement on-chain Nansen data, including parallel searches for news and prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches use a Nansen API key or selected browser session and may send intended queries through Nansen.

Mitigation: Use only for searches you intend to run through Nansen; check the selected authentication state before use.

Risk: The skill's tool allowance covers Nansen CLI commands broadly.

Mitigation: Review proposed commands and keep execution limited to the authorized search task.

## Reference(s):

- [Nansen Web Searcher on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-web-searcher)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Search-result summaries with source links; underlying CLI results are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multiple queries supported; result counts can be set from 1 to 20 per query.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
