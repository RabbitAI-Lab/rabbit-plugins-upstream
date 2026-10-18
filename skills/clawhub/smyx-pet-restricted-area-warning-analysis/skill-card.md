## Description:

Analyzes pet-monitoring footage for restricted-area entry, table climbing, and trash rummaging, and provides alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and home-monitoring users analyze footage for pets entering restricted areas or climbing on tables or rummaging through trash, and review alerts or past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive indoor pet-monitoring footage or URLs are sent to the configured lifeemergence cloud service.

Mitigation: Use only with footage you are comfortable sharing; confirm retention, deletion, and access controls before submitting sensitive video.

Risk: The skill silently creates or reuses a cloud identity and stores session tokens locally, linking report history to that identity.

Mitigation: Before use, confirm account binding, who can access past reports, and how stored tokens and reports can be removed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [JSON or text analysis report; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and optionally save results to a file.]

## Skill Version(s):

1.0.17 (source: server release metadata; bundled SKILL.md lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
