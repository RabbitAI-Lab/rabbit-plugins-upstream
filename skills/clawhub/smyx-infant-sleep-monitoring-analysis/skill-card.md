## Description:

Identifies infant sleep states from monitoring images or videos and generates structured sleep reports, schedule analysis, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers can use this skill to analyze infant sleep monitoring footage, classify sleep states such as deep sleep, light sleep, waking, and restlessness, and review generated daily sleep reports. The skill also supports querying prior cloud-hosted sleep analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles infant videos and identity data through cloud APIs.

Mitigation: Confirm the publisher documents where child videos and reports are uploaded, retained, and deleted before using sensitive nursery footage.

Risk: The security evidence flags plaintext development endpoints and non-production endpoint configuration.

Mitigation: Confirm the release is configured for production HTTPS endpoints before installation or deployment.

Risk: The security evidence flags persistent local token storage.

Mitigation: Confirm local token storage has been removed, encrypted, or otherwise secured before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file path; local video inputs are limited to mp4, avi, or mov files up to 10 MB.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
