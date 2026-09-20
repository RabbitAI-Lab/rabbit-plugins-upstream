## Description:

工程产值与进度确认表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Project managers, commercial teams, and finance teams use this skill before monthly construction output or progress confirmation to recalculate key table values, check totals, find duplicate or incomplete rows, and cite source lines for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-supplied construction output and progress table data in a local Node.js process.

Mitigation: Run it only on data you are comfortable processing locally and review the input file path before execution.

Risk: The free release omits several checks listed by the artifact, so its output may not cover every commercial review concern.

Mitigation: Treat the output as a scoped table check and use human review or the appropriate full workflow for omitted checks and contract-specific judgments.

Risk: The scanner summary says no network use, persistence, credential access, or hidden mutation behavior was found, but the script still executes local code.

Mitigation: Review and scan the artifact before deployment, and run it in a controlled environment when handling sensitive project data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/construction-output-value-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable CLI text or JSON analysis with source-referenced findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js; reports insufficient input without producing a pass/fail conclusion.]

## Skill Version(s):

1.0.53 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
