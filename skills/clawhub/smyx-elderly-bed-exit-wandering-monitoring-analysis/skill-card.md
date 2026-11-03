## Description:

Analyzes nighttime monitoring media for bed exits, prolonged wandering, and extended stillness to support caregivers' safety review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and staff in nursing homes or households use the skill to review nighttime monitoring media and query cloud-hosted reports about bed exits, wandering, or prolonged stillness. They can use the results to decide when an in-person check is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private monitoring footage may be sent for cloud processing despite the export-only setting.

Mitigation: Wait until the export-only behavior is fixed before using private footage, and confirm authorization for cloud processing and the provider's retention practices.

Risk: The skill automatically registers accounts and saves credentials.

Mitigation: Confirm that account registration is authorized and review how credentials are stored before use.

Risk: Automated monitoring results may miss or misclassify a safety concern.

Mitigation: Do not use the skill as the sole safety-monitoring system; have a caregiver check alerts in person.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured monitoring results and report links in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file; historical reports may include cloud report links.]

## Skill Version(s):

1.0.21 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
