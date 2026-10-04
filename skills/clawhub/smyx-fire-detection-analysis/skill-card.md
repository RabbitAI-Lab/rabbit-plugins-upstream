## Description:

Analyzes images and videos for flames and smoke and provides structured fire-warning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security teams and facility operators use the skill to assess images or videos for signs of fire and smoke and review previous detection reports. Its findings support early warning, not emergency response decisions without human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, and submitted URLs are sent to the configured cloud service.

Mitigation: Confirm the service, account, and media retention policy before submitting sensitive footage.

Risk: The skill creates or reuses a local cloud identity and stores account tokens locally.

Mitigation: Review which account is used, protect locally stored tokens, and establish a process to delete local SQLite data and cloud reports.

Risk: Detection results may not reliably confirm an active fire.

Mitigation: Treat findings as an early warning and have qualified personnel verify any suspected fire and follow emergency procedures.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [Fire detection API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text and report links; historical report lists in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be saved to a file; analysis results are for warning support and require human confirmation.]

## Skill Version(s):

1.0.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
