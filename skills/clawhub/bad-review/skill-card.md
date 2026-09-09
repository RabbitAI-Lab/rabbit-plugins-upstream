## Description:

Analyzes 1-3 star Amazon review feedback for a supplied ASIN to identify recurring complaint causes, review trends, and product or listing improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to inspect negative reviews, understand likely drivers of returns or rating drops, compare competitors, and prioritize listing or product fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ARI account, balance, product, review, report, alert, and workflow data through an ARI API key.

Mitigation: Install only for users who accept that access scope, keep the API key out of chat transcripts and reports, and revoke or rotate the key from the ARI account page when access is no longer needed.

Risk: Some collection, analysis, monitoring, advice, leaderboard, and export workflows can spend credits or change monitoring state.

Mitigation: Use explicit quote-only requests when evaluating cost, set autoconfirm off when every paid action should require approval, and review scheduled monitoring or competitor tracking before enabling it.

Risk: Amazon review coverage may be incomplete across marketplaces, time windows, or variants, so trend conclusions can be misleading when samples are sparse.

Mitigation: Report the sample range and collection window with conclusions, mark small samples as directional, and avoid presenting missing review data as a confirmed trend.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/bad-review)
- [ARI CLI and API Reference](references/reference.md)
- [User Guide](使用说明.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands, report links, JSON-backed summaries, and CSV or Markdown/HTML exports when supported by the ARI service.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses ARI-collected Amazon review data; paid collection, analysis, monitoring, advice, and export workflows may require user confirmation or account eligibility.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
