## Description:

Analyzes submitted pet videos or video URLs through a cloud service and returns a health report with observations, potential concerns, and a report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caregivers use the skill to request an indicative health analysis of a cat, dog, or other pet from a video or video URL, and to view past cloud reports. Its findings do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted pet media or URLs are sent to lifeemergence.com services for analysis.

Mitigation: Use only media and URLs you are comfortable sharing with that service; avoid sensitive household footage.

Risk: The skill silently creates or reuses a service identity and sends identity data to a remote login endpoint.

Mitigation: Before use with private account identifiers, ask the publisher to clarify identity ownership checks and deletion behavior.

Risk: Authentication tokens are stored in a local workspace database, and past reports are queried from the cloud.

Mitigation: Protect workspace access and confirm token retention and report access practices with the publisher.

Risk: Automated health findings may be mistaken for a veterinary diagnosis.

Mitigation: Treat findings as informational and consult a veterinarian for diagnosis or treatment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet health analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured text report with health observations, suggestions, and report links; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the report to a local file when requested.]

## Skill Version(s):

999.999.1008 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
