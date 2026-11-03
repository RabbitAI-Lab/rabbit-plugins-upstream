## Description:

Analyzes video from a pet's designated toilet area to detect a defecation event and, after the pet leaves, produce a cleaning trigger and report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use the skill to analyze footage from a designated pet toilet, retrieve prior event reports, and produce a cleaning signal for a separately configured robot vacuum workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option can still upload video.

Mitigation: Wait for this behavior to be corrected before using private household footage; review the service's data retention and deletion arrangements.

Risk: Account credentials lack adequate safeguards.

Mitigation: Review account and credential handling, and use an isolated workspace before providing sensitive data.

Risk: A vision-based event signal may trigger an unwanted cleaning action when connected to a vacuum.

Mitigation: Validate cleaning signals in an isolated setup before connecting a robot vacuum.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [API reference](artifact/references/api_doc.md)
- [Usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown, Cleaning trigger signal]

**Output Format:** [Structured JSON analysis results and Markdown history reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an event flag, timestamps, and report links; connecting a robot vacuum requires a separate smart-home gateway or vacuum API.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
