## Description:

This skill helps Amazon sellers analyze review sentiment by theme, compare positive and negative patterns, generate VOC and insight reports, monitor product changes, and export review or report files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to inspect collected Amazon reviews, identify recurring pain points and purchase motivators, compare competitors, and turn review evidence into reports or operational actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend ARI credits under account auto-confirm rules.

Mitigation: Use quote-only requests for pricing checks, set autoconfirm off when desired, and require explicit confirmation before paid actions that return confirmationRequired.

Risk: The skill requires access to an ARI account and stores an API key locally.

Mitigation: Use the browser authorization flow or a scoped API key, do not paste secrets into reports or chat, and revoke or rotate the key from the ARI account page if needed.

Risk: Recurring schedules, competitor tracking, watches, and workbench status changes can alter ongoing account behavior.

Mitigation: Explain the action and any recurring cost before enabling or changing these features, and proceed only after clear user consent.

Risk: Interrupted paid operations may already have generated a report or consumed credits.

Mitigation: Check existing reports or operation status before retrying paid collection or analysis.

Risk: Review analysis can mislead when sample size, collection window, variant coverage, or site coverage is limited.

Mitigation: State the data range and limitations in the answer, avoid inventing missing review data, and mark trends as inconclusive when evidence is insufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-sentiment)
- [User guide](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Concise text summaries, Markdown reports, JSON-backed CLI results, CSV exports, and Markdown or HTML report exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis can consume ARI credits; exported files are saved locally when requested.]

## Skill Version(s):

1.4.13 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
