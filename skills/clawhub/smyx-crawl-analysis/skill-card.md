## Description:

Analyzes reptile pet videos from local files or URLs for possible health concerns and produces a Pet Safety Guardian health report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use the skill to review reptile videos for possible health concerns, receive care suggestions, and retrieve past reports. Results are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically creates or reuses a local identity and stores authentication tokens.

Mitigation: Review the identity and token-storage behavior before installing, and protect local credentials.

Risk: Pet videos and images may be sent to lifeemergence.com services for cloud processing.

Mitigation: Use only media you are willing to send to that service.

Risk: Camera-monitoring examples are outside the core diagnosis scope and are not clearly reviewed.

Mitigation: Avoid camera-monitoring features unless their behavior and permissions have been independently reviewed.

Risk: Health analysis may be mistaken for a definitive veterinary diagnosis.

Mitigation: Treat reports as informational and consult a qualified veterinarian for diagnosis or treatment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis)
- [Reptile health analysis API documentation](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured health reports, report links, and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a report to a local file or list past reports.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
