## Description:

Through fixed cameras on aquariums, the system continuously tracks fish positions, computes the school centroid, measures each fish's distance from that centroid in body-length units, and reports prolonged isolation behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze aquarium or aquaculture camera media for schooling, loose-schooling, persistent isolation, corner-stuck behavior, and related alert levels. The skill returns behavior-focused reports and guidance without providing disease diagnoses or medication instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports that the skill can upload aquarium media or submitted URLs to remote services.

Mitigation: Use only with media the user is authorized to share, and require clear privacy, retention, and data-use disclosure from the publisher before deployment.

Risk: Security evidence reports local identity state and service tokens may be created, reused, read from the workspace, and stored in SQLite.

Mitigation: Run the skill in an isolated workspace, avoid shared machines for sensitive use, and review or clear local identity and token storage after testing.

Risk: Security evidence reports the published package is configured for private development HTTP endpoints rather than the documented cloud service.

Mitigation: Do not install or operate the release until the publisher provides corrected production configuration and documents the intended service endpoints.

## Reference(s):

- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON analysis report with alert level, isolated-fish details, recommended actions, disclaimers, and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the analysis output to a user-specified file and can list historical reports as Markdown.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact SKILL.md frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
