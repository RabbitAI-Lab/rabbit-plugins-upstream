## Description:

Analyzes submitted monitoring footage for virtual fence crossings and returns findings, alerts, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers can submit local or online monitoring footage for an on-demand review of whether a child crossed a configured safe-area boundary or approached a hazard, then receive a structured report and access historical reports. The results are an aid and do not replace direct supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private baby-monitoring footage or account access could be exposed while destination override, environment-only mode, and credential destination restrictions remain unresolved.

Mitigation: Do not submit private footage until those fixes are in place. Review the provider's retention and deletion terms, and account for credentials and accounts persisting locally.

Risk: An on-demand analysis could be mistaken for continuous safety monitoring.

Mitigation: Use results only as an auxiliary alert; maintain direct supervision and do not rely on the skill for continuous alerts.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report or historical report list, in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection findings, recommendations, timestamps, and report links.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
