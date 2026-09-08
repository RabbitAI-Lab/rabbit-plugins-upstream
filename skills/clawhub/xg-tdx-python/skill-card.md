## Description:

小果通达信公式转Python helps agents convert Tongdaxin (TDX) formula logic into pandas/numpy Python functions and use a library of technical indicators and trading-strategy signal templates for analysis and backtesting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative analysts use this skill to migrate TDX indicator formulas into Python, compute technical indicators, and produce strategy signal DataFrames for backtesting, data analysis, and trading-signal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Converted or generated Python may write local files or produce executable analysis code.

Mitigation: Use explicit input and output paths, keep generated files in a working directory, and review generated Python before running it.

Risk: Trading signals may be mistaken for automatic trading advice.

Mitigation: Treat outputs as analysis and backtesting material, validate results independently, and avoid automatic trading decisions without separate controls.

Risk: Some functions documented in the artifact use future data and are marked unsuitable for live trading.

Mitigation: Restrict future-data functions such as BACKSET, ZIG, PEAK, and TROUGH to review or retrospective analysis, and remove them from live workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-tdx-python)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with Python code examples and formula mappings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces pandas/numpy-oriented functions, indicator outputs, strategy signal DataFrames, and local file conversion guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
