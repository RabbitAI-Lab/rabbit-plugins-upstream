## Description:

This skill analyzes aquarium plant images or videos to detect visible health symptoms and produce a structured assessment with care-direction suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarium operators, aquascapers, and aquarium shops use this skill to analyze aquarium plant images or videos for visible leaf color, morphology, algae, and deficiency symptoms. The skill returns a health assessment, likely cause categories, care-direction suggestions, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports unsafe cloud communication and local credential handling that are not suitable for normal installation.

Mitigation: Review before installing; require HTTPS-only approved service hosts and avoid plaintext token storage before deployment.

Risk: Security evidence reports that media upload and report retrieval are not explained clearly enough for user control.

Mitigation: Document what media is uploaded, how reports are retrieved, and what user or operator approval is required before use.

Risk: Security evidence reports a dependency naming issue.

Mitigation: Fix dependency declarations before normal installation or packaging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [Aquarium Plant Health Monitor API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON text with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured analysis results, health status, care suggestions, historical report tables, and report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
