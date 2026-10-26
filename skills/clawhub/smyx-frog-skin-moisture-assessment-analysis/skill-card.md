## Description:

Assesses frog skin moisture from images or video and provides structured observations and dehydration-risk alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Frog keepers, amphibian facilities, and veterinary teams use the skill to review enclosure photos or videos for changes in skin moisture and request past assessment reports. Results support monitoring, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media or URLs are processed by a configured cloud service.

Mitigation: Confirm the service destination and obtain approval before submitting sensitive media or URLs.

Risk: The skill automatically creates or logs in to a backend identity and stores user records and tokens locally, with limited user control.

Mitigation: Review account creation and local token and record retention before installation; restrict access to stored credentials and records.

Risk: Image-based moisture assessments may be unreliable and could be mistaken for veterinary diagnosis.

Mitigation: Treat alerts as screening guidance, reject poor-quality images, and consult an amphibian veterinarian for serious concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Text or JSON analysis report; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk alerts, recommendations, and a report-export link]

## Skill Version(s):

1.0.12 (source: ClawHub release; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
