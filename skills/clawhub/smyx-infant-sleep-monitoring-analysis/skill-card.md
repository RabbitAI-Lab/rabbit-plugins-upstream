## Description:

Identifies infant sleep states such as deep sleep, light sleep, waking, and restlessness, then generates daily sleep reports and schedule analysis to help caregivers understand sleep patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers can use this skill to analyze infant sleep-monitoring videos or URLs, classify sleep states, generate structured reports, and query prior cloud reports. Results are for parenting reference and should not replace professional medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant sleep videos or video URLs may be sent to LifeEmergence cloud services for analysis.

Mitigation: Use the skill only with appropriate consent and data-handling approval, and avoid submitting unnecessary or highly sensitive footage.

Risk: Report-history prompts can trigger cloud report queries tied to the current identity.

Mitigation: Review prompts before execution and use the skill only in workspaces where automatic cloud history lookup is acceptable.

Risk: The skill can create or reuse a local identity and store session tokens in a workspace SQLite database.

Mitigation: Run it in an isolated workspace or account and clear local session data when access should no longer persist.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Analysis API error-code documentation](skills/smyx_analysis/references/api_doc.md)
- [LifeEmergence skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown report or JSON output, with optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sleep-state results, schedule analysis, recommendations, report links, and historical report tables.]

## Skill Version(s):

1.0.8 (source: server release metadata; SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
