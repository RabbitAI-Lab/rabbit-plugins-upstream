## Description:

Builds a US competitor analysis report from your own notes, with a fixed section structure and a source log for every figure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

US small business owners, product managers, and sales leads use the skill to turn their own competitor notes into internal profiles, comparisons, dated source logs, and a list of unverified items.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Figures and cited sources in the generated report may be inaccurate or misleading if left unchecked.

Mitigation: Manually verify each figure and its source and capture date before relying on or sharing the report.

Risk: Running the script can overwrite an existing digest.md in the output directory.

Mitigation: Use a fresh output directory or back up any existing digest.md first.

Risk: The optional Windows executable has not been reviewed and is not needed for the Python workflow.

Mitigation: Use the Python workflow; do not run the optional executable unless you independently review and accept it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rapidworker1/skills/competitor-analysis-report)
- [Publisher homepage (skill metadata)](https://github.com/rapidworker1)
- [US competitive analysis reference](artifact/references/competitive-analysis.md)
- [Competitor brief template](artifact/templates/competitor-brief.yaml)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown digest with market context, competitor profiles, comparison matrix, pricing notes, source log, and open questions.]

**Output Parameters:** [One notes file; optional output directory.]

**Other Properties Related to Output:** [Keeps missing-source items unverified rather than filling them by guesswork. Processes notes locally; digest.md is overwritten if it already exists in the output directory.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter, server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
