## Description:

Generates audience-specific QA test reports, including daily updates, weekly summaries, iteration reports, quality status, defect analysis, risk assessment, and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, project managers, and stakeholders use this skill to turn test execution data, defect data, and quality metrics into daily, weekly, iteration, and specialized QA reports tailored to the intended audience.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad prompts such as daily report or progress report could activate a QA-style report when the user intended a general status report.

Mitigation: Confirm the user wants a QA or test-reporting format before applying the skill to generic reporting requests.

Risk: Example report fields may include release or delay recommendations that could be mistaken for authorization to make release decisions.

Mitigation: Treat release and delay language as report content for authorized reviewers, not as an instruction to execute product release decisions.

Risk: The skill advertises a larger QA skill set installation command that may change the agent environment.

Mitigation: Review the larger QA skill set before running the advertised npx install command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-reporting)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown reports with tables, checklists, summaries, risk assessments, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report depth and structure vary by audience and report type; outputs are intended for workspace files and stakeholder review.]

## Skill Version(s):

1.7.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
