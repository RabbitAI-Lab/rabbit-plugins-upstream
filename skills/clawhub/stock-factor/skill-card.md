## Description:

Stock Factor provides collected and transcribed A-share stock factor lists that an agent can read as Excel outputs or run through QuantAll task JSON for IC, IR, and time_potential analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and quantitative research users use this skill to inspect A-share stock factor libraries, run bundled QuantAll task JSON, and review IC, IR, and time_potential outputs for candidate factor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the external QuantAll package with a local stock database can expose local market data to the local analysis engine.

Mitigation: Install and run the skill only in an environment where that local engine and database access are acceptable.

Risk: Batch updates write result files to configured output paths and can overwrite or misplace factor results if paths are not reviewed.

Mitigation: Check task JSON save paths before running updates and keep separate output directories for experiments.

Risk: Factor IC, IR, and time_potential values are research signals and may be incomplete or misleading for direct trading decisions.

Mitigation: Treat outputs as candidate research inputs and validate factors with additional review, correlation checks, and strategy backtests before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mifochen/skills/stock-factor)
- [Skill source documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON task files, Python snippets, shell commands, configuration examples, and Excel factor result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bundled task JSON targets QuantAll batch factor analysis and writes results to configured output paths.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
