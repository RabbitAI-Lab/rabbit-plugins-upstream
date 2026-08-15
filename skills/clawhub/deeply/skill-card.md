## Description:

Evidence Api retrieves dated, sourced first-person expert viewpoints from deeply's offline corpus for judgment-oriented finance, technology, business, and ideas questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[komako-workshop](https://clawhub.ai/user/komako-workshop)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user is weighing a judgment and needs sourced expert perspectives, including contrary viewpoints. It is intended for judgment questions over the deeply.dev corpus, not current prices, breaking news, or topics outside its coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User questions may be sent to the external deeply.dev API under broad activation guidance without clear user consent.

Mitigation: Tell users when their query will be sent to deeply.dev and avoid sending confidential, personal, regulated, or sensitive business details unless the user is comfortable sharing them with that service.

Risk: The skill can be mistaken for a current-facts lookup even though its evidence corpus is offline and not suited to breaking news or live prices.

Mitigation: Use it for sourced judgment evidence and use a current source for time-sensitive facts, prices, schedules, or recent news.

Risk: Token setup and API access depend on a third-party provider.

Mitigation: Verify the deeply.dev provider and token command before installation, and stop retrying after authentication failures until the user has corrected the token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/komako-workshop/skills/deeply)
- [Deeply](https://deeply.dev)
- [Evidence search API](https://api.deeply.dev/v2/evidence/search)
- [Evidence unit API](https://api.deeply.dev/api/unit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses DEEPLY_TOKEN for authenticated API calls; search supports top-k retrieval, reranking, per-person caps, and optional as-of filtering.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
