## Description:

Analyzes video from a pet's designated toilet area, reports defecation events, and outputs a cleaning trigger after the pet leaves.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners can use the skill to review video from a designated pet toilet area, identify defecation events, and receive a cleaning trigger and report. The trigger is an event signal; connecting it to a robot vacuum requires a user-side smart-home gateway or vacuum API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential forwarding, account registration, and account storage are not clarified in the supplied security guidance.

Mitigation: Clarify what credentials are forwarded and how accounts are created and stored before installation; defer use until these details are resolved.

Risk: Video may be uploaded for external processing.

Mitigation: Disclose external video processing and obtain appropriate consent before submitting footage.

Risk: Reported analysis behavior conflicts with modes that claim not to analyze.

Mitigation: Confirm the actual processing behavior and treat those mode claims as unverified until clarified.

Risk: The security scan is partial because a referenced local path was missing, leaving some imported components and behavior unassessed.

Mitigation: Review the missing path and unassessed imported components before relying on the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [JSON analysis reports and Markdown history tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event status, timestamps, suggestions, and a report link. A cleaning trigger is an event signal and does not itself control a robot vacuum.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
