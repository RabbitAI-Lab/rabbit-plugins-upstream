## Description:

Fetches and analyzes content from supplied URLs using Nansen's AI-powered web fetch command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users provide one or more URLs and a question to retrieve and summarize web content or compare pages.

### Deployment Geography for Use:

Global, subject to applicable account, sanctions, and geographic checks.

## Known Risks and Mitigations:

Risk: The Nansen CLI uses a Nansen API key or selected browser session for URL analysis.

Mitigation: Install only if Nansen account access is intended, and review the nansen-cli package provenance before use.

Risk: Submitted URLs or questions may contain sensitive information.

Mitigation: Do not submit secrets in URLs or questions unless that matches your Nansen account's data-handling expectations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-web-fetcher)
- [ClawHub publisher profile](https://clawhub.ai/user/nansen-devops)
- [Nansen CLI browser-login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [JSON with an analysis answer and retrieved/failed URL lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 20 URLs per fetch; inaccessible pages may appear in failed_urls.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
