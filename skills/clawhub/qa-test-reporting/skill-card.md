## Description:

Generates audience-specific QA test reports, including daily updates, weekly summaries, iteration reports, and quality reports that summarize progress, defects, risks, and release recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, project managers, and release stakeholders use this skill to turn test execution data and defect data into concise reports for team synchronization, project tracking, quality assessment, and release decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic prompts for daily, weekly, or report templates may activate this QA reporting skill outside a testing or quality context.

Mitigation: Confirm the request is about test execution, quality data, or QA reporting before applying the skill.

Risk: Generated release or delay recommendations could be mistaken for an authorized release decision.

Mitigation: Treat release recommendations as report content for stakeholder review, and require the normal approval process before acting on them.

Risk: Reports can mislead stakeholders if source test execution data, defect counts, or quality metrics are incomplete or stale.

Mitigation: Verify the input data and call out missing or uncertain metrics in the report rather than filling gaps with unsupported conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-reporting)
- [Publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report templates and concise narrative guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include structured sections for progress, quality metrics, defect analysis, risk assessment, recommendations, traceability IDs, and next steps.]

## Skill Version(s):

1.6.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
