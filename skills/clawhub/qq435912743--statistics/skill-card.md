## Description:

Analyzes CSV or JSON datasets with descriptive statistics, Pearson correlations, and optional two-sample Welch t-tests using only Python standard library tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data analysts use this skill to run lightweight offline statistical summaries on tabular datasets, inspect numeric correlations, and compare two groups when a Welch t-test is appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learner can persist local history, notes, errors, preferences, and recent operations, including for another skill directory if invoked with that path.

Mitigation: Avoid sensitive dataset details in learner notes, disable or remove the learner when persistent usage tracking is not needed, and review learned_patterns.json before sharing artifacts.

Risk: Statistical results can be misleading when datasets are malformed, sample sizes are too small, numeric columns are sparse, or Pearson correlation and Welch t-test assumptions do not fit the data.

Mitigation: Inspect input data quality, sample sizes, missing values, and test assumptions before using the generated summaries for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/statistics)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [JSON summaries with concise Markdown or text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write a JSON summary file with scripts/stats.py --out; the learner utility can persist local usage state.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
