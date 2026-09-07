## Description:

Helps Amazon sellers and operators list pending negative reviews, generate buyer reply language, appeal suggestions, and product-improvement recommendations, and track each review's handling status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to inspect review data, prioritize negative-review handling, draft replies or appeals, generate VOC and keyword-style reports, compare competitors, and manage related monitoring workflows through an ARI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The narrowly named review-reply helper also supports paid analyses, persistent monitoring, competitor binding, broad local exports, and account confirmation-setting changes.

Mitigation: Review the scope before installing, use only an ARI account you trust, keep confirmations enabled for paid actions unless deliberately changed, and require explicit user consent for monitoring, competitor binding, exports, and autoconfirm changes.

Risk: Analysis and recommendations can be overconfident when collected review samples, marketplace coverage, variants, or time windows are limited.

Mitigation: State the sample size, marketplace, collection window, and known gaps in each response; treat small samples and single reviews as directional signals rather than definitive evidence.

Risk: Exports write files locally and paid operations may have already charged credits if a stream or network connection is interrupted.

Mitigation: Use trusted export paths, preserve existing results on failure, and check the latest report or task status before retrying any paid operation.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [ARI Amazon Review Assistant Usage Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/review-reply)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON returned by the ARI CLI, with optional local CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key or browser authorization. Outputs may include review summaries, reply and appeal drafts, product recommendations, report links, credit usage, and account-specific status.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, CHANGELOG, evidence release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
