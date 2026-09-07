## Description:

ARI Amazon review intelligence skill for collecting and analyzing Amazon reviews, generating VOC or deeper insight reports, and producing consumer pain points, purchase motivations, user personas, usage scenarios, product improvement opportunities, and Listing recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, operators, and supporting agents use this skill to analyze ASIN review data, understand customer complaints and buying motivations, compare competitors, monitor review changes, export review/report files, and turn review evidence into listing and product-improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits through review collection, VOC/deep analysis, leaderboard, operations, and advise workflows, and some flows may auto-confirm under account rules.

Mitigation: Set the account to ask before each credit charge or request quote-only operation, and require explicit confirmation before paid commands or autoconfirm changes.

Risk: The skill uses an ARI account key and can export review/report files or manage ongoing monitoring settings.

Mitigation: Keep the API key out of chat transcripts and reports, review export destinations, and confirm schedule, watch, competitor, and monitoring changes before execution.

Risk: Interrupted paid operations may already have consumed credits and created reports, so immediate retries can duplicate charges.

Mitigation: Check existing reports or operation status before rerunning any paid command after a timeout or stream interruption.

Risk: Review analysis is limited to ARI-collected data and may not cover all Amazon reviews, variants, or enough history for trend claims.

Mitigation: Present sample size, site, collection window, and data gaps with every analysis, and avoid unsupported trend or variant conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/sellerari)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [ARI CLI and API reference](references/reference.md)
- [ARI account and authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-backed CLI results, with optional local CSV, Markdown, or HTML exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ASIN/site scope, sample size, review evidence, report IDs, report URLs, credit usage, balance information, and local export paths.]

## Skill Version(s):

1.4.7 (source: server release metadata, artifact/SKILL.md frontmatter, artifact/_meta.json, artifact/scripts/ari.py, artifact/CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
