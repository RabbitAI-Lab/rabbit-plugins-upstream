## Description:

Analyzes cat litter-box videos to track each cat's visit frequency and duration, compare behavior with historical baselines, and flag unusual patterns as non-diagnostic urinary-health alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Cat owners, catteries, veterinary wards, and boarding centers use the skill to review litter-box videos, track each cat's visit frequency and duration, and compare behavior with historical patterns for non-diagnostic alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious due to reported credential and account handling, behavior beyond its stated cat-video analysis purpose, and uncertainty about analysis triggered by export-only options.

Mitigation: Before installation or use, verify where credentials and identity data are sent and stored, whether uploaded videos are processed remotely, and whether export-only use can trigger analysis.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report; JSON results; Markdown history listing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-cat visit frequency and duration, historical comparisons, behavior alerts, and report links. Alerts are not medical diagnoses.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; packaged SKILL.md frontmatter says 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
