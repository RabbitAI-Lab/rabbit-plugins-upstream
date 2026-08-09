## Description:

WorkBuddy Usage Status turns local WorkBuddy usage data into an offline dashboard for token consumption, thinking time, thinking efficiency, model distribution, errors, and credit consumption.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users and developers use this skill to audit local usage, costs, model behavior, errors, and efficiency from their own WorkBuddy data. It supports local cost control and usage review by generating an offline dashboard and machine-readable aggregate data files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports can reveal local usage history, session titles, model choices, costs, timestamps, and error summaries if shared or synced.

Mitigation: Run the skill deliberately, write output to a folder you control, and review generated HTML, JSON, and JavaScript files before sharing them.

Risk: The skill reads local WorkBuddy data under the selected WorkBuddy home directory.

Mitigation: Use the default local home or an explicit --home path only for data you intend to analyze; the scanner evidence reports no artifact evidence of exfiltration or destructive behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [Chart.js](https://www.chartjs.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, code, guidance]

**Output Format:** [Markdown guidance with shell commands; generated artifacts are HTML, JSON, and JavaScript files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated dashboard is self-contained and offline, with Chart.js and usage data inlined into the HTML output.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
