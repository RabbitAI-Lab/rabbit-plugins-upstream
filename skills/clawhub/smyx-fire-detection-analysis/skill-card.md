## Description:

Real-time detection of flames and smoke in video and image scenes for fire early warning in industrial parks, forests, warehouses, and other locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze camera images, videos, or media URLs for flame and smoke indicators, retrieve structured fire-risk reports, and review historical detection reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media, media URLs, and historical report queries are processed through LifeEmergence cloud services.

Mitigation: Review before installing in shared or sensitive camera environments, and deploy only where remote processing and account linkage are acceptable.

Risk: The skill silently creates or reuses an identity and stores service tokens in the workspace data directory.

Mitigation: Run the skill in a controlled workspace, restrict access to the data directory, and rotate or remove persisted credentials when decommissioning the skill.

Risk: Fire and smoke analysis can support alerts but should not be treated as a final emergency determination.

Mitigation: Use results as an early-warning aid and require human or professional confirmation for emergency response decisions.

## Reference(s):

- [Fire Detection API documentation](references/api_doc.md)
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured analysis content, report links, and JSON-formatted report data when available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail modes; can optionally write the rendered result to a local output file.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
