## Description:

Monitor Reddit, Hacker News, X, and Bluesky for keyword mentions of a product or website using the RedReplier API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and growth teams use this skill to monitor product and website mentions across Reddit, Hacker News, X, and Bluesky, then triage AI-scored mentions as potential leads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedReplier API token that grants account-level access to monitoring data.

Mitigation: Use a dedicated, revocable token and send it only to the fixed RedReplier API host.

Risk: Manual API actions can activate billing upgrades or delete monitored websites.

Mitigation: Require a preview, exact target, cost details, and explicit user confirmation before any billing activation or deletion.

Risk: URL analysis may expose private or internal site details to the SaaS service.

Mitigation: Avoid URL-analysis features for private or internal sites unless the user has approved that disclosure.

Risk: AI-scored mentions can be wrong or incomplete.

Mitigation: Review the actual mention content and relevance explanation before approving or rejecting leads.

## Reference(s):

- [RedReplier API Reference](artifact/references/api-reference.md)
- [Mention Filtering Reference](artifact/references/mention-filtering.md)
- [RedReplier Website](https://redreplier.com)
- [ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/redreplier)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API response summaries and explicit confirmation prompts before billing or deletion actions.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
