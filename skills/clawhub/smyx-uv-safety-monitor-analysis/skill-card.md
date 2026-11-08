## Description:

Analyzes submitted video or video URLs for signs of pets in UV disinfection areas and returns structured safety reports and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and pet boarding staff can submit video for analysis of possible pet entry into UV disinfection areas and review the resulting safety report and history. Treat the output as advisory; it does not establish that a UV lamp has been shut off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The analysis may not reliably detect a hazard or shut off a UV lamp.

Mitigation: Treat reports as advisory, verify lamp state directly, and use an independent safety control rather than relying on this skill for shutdown.

Risk: Household videos may be uploaded to an external service, including when the configuration-only option is selected; account enrollment and footage retention details need clarification.

Mitigation: Before installing, confirm upload choices, account enrollment, footage retention and deletion, and protected credential storage; avoid submitting sensitive footage until these are clear.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [API interface reference](artifact/references/api_doc.md)
- [Skill introduction and usage examples](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, JSON, Markdown]

**Output Format:** [Structured analysis reports and report links; history results are returned as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety observations, recommendations, and cloud report history.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
