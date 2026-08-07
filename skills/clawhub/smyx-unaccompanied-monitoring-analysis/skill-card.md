## Description:

Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care operators use this skill to analyze home monitoring images or videos for prolonged lack of interaction or visitors. Agents can also query vendor-hosted historical reports and return care reminders, report summaries, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home monitoring images, videos, report queries, and identity-linked request metadata may be sent to vendor cloud services.

Mitigation: Confirm consent from monitored people and family recipients before use, and use the skill only for the intended elder-care monitoring scenario.

Risk: Cloud report history, automatic identity creation, and stored tokens may expose sensitive care records if storage or access controls are not reviewed.

Mitigation: Verify where reports and tokens are stored, who can access them, and how they are removed before enabling the skill in a real care workflow.

Risk: The security summary reports too little user-facing control or privacy disclosure for sensitive elder-care footage.

Mitigation: Run human privacy and security review before deployment and avoid analyzing unrelated private footage.

## Reference(s):

- [Unattended Monitoring Skill on ClawHub](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports and tables, JSON API results, and shell commands for analysis or report lookup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, care recommendations, and historical report rows returned from vendor cloud services.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
