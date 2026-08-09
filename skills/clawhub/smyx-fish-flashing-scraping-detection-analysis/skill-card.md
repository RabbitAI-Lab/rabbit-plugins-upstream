## Description:

Analyzes fixed aquarium camera images or videos to detect fish flashing or scraping behavior, count abnormal friction frequency, and produce ectoparasite risk warnings when configured thresholds persist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarists, aquarium operators, aquaculture teams, and developers use this skill to analyze aquarium or pond media for flashing and scraping behavior, review structured warning reports, and query prior cloud-hosted reports. It supports early risk screening and escalation guidance, not veterinary diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media and history queries are processed through lifeemergence/open.lifeemergence cloud APIs.

Mitigation: Get explicit user confirmation before uploading media or querying history, and avoid submitting sensitive footage unless the user accepts the cloud-processing exposure.

Risk: The skill may silently create or reuse a local service identity and store returned service tokens in a workspace SQLite database.

Mitigation: Review identity and token storage behavior before installation, restrict workspace access, and verify how to delete local identity, token, and remote report data.

Risk: Behavior-based ectoparasite warnings could be mistaken for a diagnosis or treatment plan.

Mitigation: Present results as screening guidance only, avoid medication or dosing instructions, and direct users to inspect fish and consult a qualified aquatic veterinarian for microscopy-based diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis reports with warning status, observed friction metrics, recommended actions, history tables, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the analysis output to a user-selected file path when requested.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
