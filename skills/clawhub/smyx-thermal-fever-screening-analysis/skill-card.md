## Description:

Analyzes thermal-camera images or video of groups for relative skin-temperature differences and produces screening alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families and operators of shared spaces can use this skill to screen thermal-camera footage for relative temperature differences and review analysis reports. Treat alerts as a prompt for rechecking with a calibrated thermometer, not as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unclear account and credential handling, remote destinations, local video uploads, and behavior associated with --export-env-only; thermal footage may contain sensitive personal and health information.

Mitigation: Avoid installation or uploading footage until the maintainer clarifies account and credential handling, remote destinations, and the behavior of --export-env-only. Obtain participants’ informed consent before processing their footage.

Risk: Relative thermal screening can be affected by clothing, activity, nearby heat sources, or limited visible forehead samples, and does not establish a medical diagnosis.

Mitigation: Use alerts only as a screening prompt and recheck with a calibrated thermometer; seek clinical assessment where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis)
- [Thermal screening API reference](artifact/references/api_doc.md)
- [API error codes](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured screening results and report links, available as JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include relative temperature differences, screening alerts, recommendations to recheck, and links to reports.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
