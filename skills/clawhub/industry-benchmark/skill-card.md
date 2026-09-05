## Description:

This skill helps Amazon sellers use ARI to compare an ASIN against category star-rating and negative-review benchmarks, inspect category leaderboards, and produce review-analysis guidance from collected Amazon review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to benchmark product star ratings and negative-review rates, review category rankings, monitor reviews, and generate concise operational reports and exports through ARI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI paid actions can spend credits, and server-side auto-confirm may allow small paid actions to run without another prompt in the current chat.

Mitigation: Review auto-confirm settings after setup, prefer autoconfirm off for strict approval workflows, and check balance or quote output before paid collection, analysis, or leaderboard actions.

Risk: Interrupted paid operations may already have spent credits or archived a report before the local command reports a timeout or network error.

Mitigation: Use the free report/status lookup for the same ASIN or request ID before retrying a paid command.

Risk: The skill handles an ARI API key for authenticated account workflows.

Mitigation: Store the key only in ARI_API_KEY or the local user ARI config, avoid putting it in reports or examples, and review exports before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/industry-benchmark)
- [ARI API and CLI reference](references/reference.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI products](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)
- [ARI billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON summaries, shell command snippets, and local report/export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local Markdown, HTML, or CSV exports and may include ARI report URLs when returned by the service.]

## Skill Version(s):

1.4.5 (source: server release evidence, artifact frontmatter, _meta.json, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
