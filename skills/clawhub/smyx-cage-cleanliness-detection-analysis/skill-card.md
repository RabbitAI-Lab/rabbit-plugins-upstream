## Description:

Analyzes cage images or videos to estimate feces and urine coverage, score cleanliness, and return cleaning alerts for pet boarding, pet shop, veterinary, and breeding-facility settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers can use this skill to submit cage images, videos, or media URLs for cleanliness analysis, structured reports, and historical report lookup. It supports pet boarding centers, pet shops, animal hospitals, and breeding facilities that need cleaning alerts based on visual waste coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends cage images, videos, URLs, and account-linked identifiers to the LifeEmergence/SMYX backend for analysis.

Mitigation: Install only if that backend is trusted, use approved media, and avoid sensitive facility footage unless disclosure is authorized.

Risk: The security evidence reports automatic cloud account/login behavior and local storage of identity tokens with limited user-facing control.

Mitigation: Review or change endpoint configuration before use and clear workspace data database or token files when identity reuse is not wanted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the report text to a file when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
