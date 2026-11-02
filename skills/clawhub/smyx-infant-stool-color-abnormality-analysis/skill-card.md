## Description:

Analyzes images of infant stool to classify color, flag potential abnormalities, and provide screening guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families, pediatric clinics, and postpartum care teams use the skill to review infant stool images for color abnormalities and receive screening guidance. It can also support integration into parenting apps and infant-care devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-analysis option may still submit sensitive infant images, and cloud retention, account registration, credential storage, and deletion are unclear.

Mitigation: Before supplying imagery, confirm the no-analysis behavior is fixed and obtain clear information about retention, account handling, credentials, and deletion. Use dedicated credentials and avoid shared default accounts.

Risk: Image color can be misread under tinted lighting or filters, and the result is screening guidance rather than a medical diagnosis.

Mitigation: Use natural or cool white light without filters, treat results only as screening information, and seek clinical evaluation for concerning results; the skill directs immediate care for clay-pale results.

Risk: Infant diaper and stool images contain sensitive information about a child.

Mitigation: Obtain a guardian's informed consent before use and store images securely.

## Reference(s):

- [Infant Stool Color Analysis API Reference](references/api_doc.md)
- [Analysis API Details](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Files]

**Output Format:** [Structured analysis report with color classification, risk guidance, and a report link; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; accepts a local image file or image URL.]

## Skill Version(s):

1.0.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
