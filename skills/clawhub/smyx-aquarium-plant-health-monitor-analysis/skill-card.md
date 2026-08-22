## Description:

Analyzes aquarium plant images, videos, or URLs to identify visual health issues and return structured health assessments with care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarium hobbyists, aquascaping shops, and developers operating ClawHub agents use this skill to submit aquarium plant media for visual health assessment, likely causes, care direction, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media or URLs may be sent to the LifeEmergence cloud service.

Mitigation: Use only media and URLs that are appropriate for third-party processing, and avoid submitting sensitive imagery unless retention and access controls are clarified.

Risk: The skill may link analysis activity to an automatically selected local identity and store account or token data locally.

Mitigation: Run the skill in an isolated workspace and review or clear data/smyx-api-key.txt and any smyx-common SQLite database before and after use.

Risk: Cloud report links and historical report queries may expose prior analysis results associated with the local identity.

Mitigation: Treat generated report links and history output as sensitive, and confirm account controls with the publisher before commercial deployment.

Risk: Visual plant-health assessments can be uncertain when symptoms overlap or image quality is poor.

Mitigation: Use the output as advisory guidance and confirm care decisions with water tests, direct inspection, or an aquarium specialist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include health assessment details, care suggestions, report export links, and historical report lists returned by the cloud API.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
