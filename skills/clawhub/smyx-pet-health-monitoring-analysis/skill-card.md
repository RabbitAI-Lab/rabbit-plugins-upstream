## Description:

Analyzes pet monitoring images and videos for feeding, drinking, elimination, activity, vomiting, and limping patterns, then returns health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and caretakers use the skill to review monitoring footage for changes in everyday behavior and retrieve past health reports. Its findings are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet monitoring media or URLs are sent to a cloud service, and stored reports may be retrieved without clear user-facing data controls.

Mitigation: Obtain informed consent before submitting media or retrieving reports; review the cloud service's data handling before use.

Risk: The skill may silently create or reuse an online identity and store access tokens in a workspace database.

Mitigation: Review identity creation and local credential storage before installation; restrict workspace access and protect stored tokens.

Risk: Automated health findings may be mistaken for a veterinary diagnosis.

Mitigation: Treat findings as informational and consult a veterinarian about concerning symptoms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)
- [Pet health analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Health report in JSON or Markdown; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior findings, risk alerts, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
