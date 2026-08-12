## Description:

AI-powered cage cleanliness detection via fixed cameras in boarding kennels and pet shops; analyzes floor images to detect feces or urine coverage area ratio and trigger cleaning alerts when coverage exceeds a preset threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators of pet boarding centers, pet shops, animal hospitals, and breeding facilities use this skill to analyze cage floor images or videos for feces and urine coverage, cleanliness scoring, cleaning alerts, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cage images, videos, report queries, and generated reports are sent to configured lifeemergence.com cloud services.

Mitigation: Use the skill only with media and report data approved for that service, and confirm retention, deletion, and access-control expectations before using sensitive content.

Risk: The skill creates or reuses a local identity and stores service tokens in a workspace SQLite database.

Mitigation: Run in a controlled workspace, protect or remove the local database after use, and verify identity and token retention behavior before deployment.

Risk: Cleanliness analysis is based on visual estimation and is not a medical or veterinary diagnosis.

Mitigation: Treat results as hygiene management signals and route health concerns to qualified staff or veterinarians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Pet cage cleanliness API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with cleanliness results, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the generated report to a user-specified output file.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
