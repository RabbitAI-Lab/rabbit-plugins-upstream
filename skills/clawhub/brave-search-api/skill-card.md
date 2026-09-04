## Description:

Brave Search API integration with managed authentication for web, image, news, video, local, autosuggest, spellcheck, and summary search through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Brave web, image, news, video, local, autosuggest, spellcheck, and summary endpoints through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill authorizes Brave Search access through Maton and can make Brave Search API calls.

Mitigation: Install it only when that access is acceptable, prefer OAuth, and confirm each new Brave Search connection yourself.

Risk: Broad passthrough API behavior can make the target connection or operation ambiguous.

Mitigation: Require explicit confirmation before non-read requests and specify the intended connection when more than one Brave Search connection exists.

Risk: Raw API-key use can expose a long-lived credential if it is printed, logged, or passed through the shell.

Mitigation: Use OAuth where possible; if an API key is necessary, avoid printing, logging, persisting, or passing it on a command line.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Maton Homepage](https://maton.ai)
- [Brave Search API Documentation](https://api-dashboard.search.brave.com/documentation)
- [Brave Search API Dashboard](https://api-dashboard.search.brave.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Brave Search connection; calls may be rate limited by Maton or Brave Search.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
