## Description:

This skill analyzes resting pet video or image inputs to estimate respiratory rate, compare the result with species and body-size resting ranges, and return abnormality warnings, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, veterinary staff, and boarding-center operators use this skill to analyze resting pet footage for respiratory-rate abnormalities and review current or historical structured reports. Results are health-reference warnings, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet video files or URLs are sent to the configured analysis service and account-linked report history can be fetched.

Mitigation: Use only media appropriate for that service, confirm user consent for report retrieval, and avoid submitting sensitive or unnecessary footage.

Risk: The skill can create and reuse local identity and token records without prompting the user.

Mitigation: Review where identity and token data are stored, limit local access to those records, and clear them when the skill is no longer needed.

Risk: Packaged development configuration includes private or debug API endpoints.

Mitigation: Verify and correct endpoint configuration before installation or execution in a production environment.

Risk: Respiratory-rate outputs are health-reference warnings rather than clinical diagnoses.

Mitigation: Present results as screening guidance and direct users to seek veterinary evaluation for persistent or severe abnormalities.

## Reference(s):

- [Respiratory-rate analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown text with embedded structured JSON and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and may write a user-requested output file.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
