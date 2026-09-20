## Description:

年终奖分配表逐项核对，每条结论都带原文行号，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, finance, and operations users can use this skill to locally check Chinese annual bonus allocation worksheets before review or payout. It recalculates bonus-pool allocation, annual one-time bonus tax, net bonus, totals, duplicates, and blanks, then reports findings with source line numbers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool processes payroll-like compensation data supplied by the user.

Mitigation: Run it only in an environment appropriate for sensitive employee compensation data and avoid sharing source worksheets beyond the intended local workflow.

Risk: The annual bonus tax checks rely on the bundled static assumptions and are not tax advice.

Mitigation: Verify the tax assumptions and results against the user's current payroll and tax requirements before using findings for payout or filing decisions.

Risk: Materials that are incomplete or missing required worksheet headers cannot support a reliable conclusion.

Mitigation: Provide the worksheet with recognizable headers and review any missing-field response before treating the check as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bonus-pool-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Console text or JSON findings with summaries, check lists, omitted checks, and line-cited issues]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided bonus worksheet text or JSON input; insufficient input returns missing fields rather than a pass/fail conclusion.]

## Skill Version(s):

1.0.54 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
