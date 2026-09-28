## Description:

Search the web for one or more queries in parallel to complement on-chain Nansen data with current information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can search for current news, prices, and web content alongside on-chain Nansen research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a CLI package without checking its provenance can introduce an unintended dependency.

Mitigation: Confirm the nansen-cli package provenance before installation.

Risk: Web searches use the configured Nansen API key or selected browser session.

Mitigation: Use only credentials and session access appropriate for the search task; stop if authentication fails.

## Reference(s):

- [Nansen Web Searcher on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-web-searcher)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of web search results and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts multiple queries and 1–20 results per query.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
