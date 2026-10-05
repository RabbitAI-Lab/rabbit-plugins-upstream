## Description:

Helps developers look up allowed OOXML elements, attributes, values, and child order, and interpret schema validation errors in Word, Excel, and PowerPoint documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers editing or debugging the XML inside .docx, .xlsx, or .pptx files use this skill to check schema constraints and understand validation errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw read-only SQL queries can still consume resources during broad database exploration.

Mitigation: Keep queries user-directed and focused on schema lookup; prefer the dedicated lookup commands.

Risk: Using the default Transitional profile for a Strict OOXML document can lead to incorrect schema guidance.

Mitigation: Check the document's namespaces and select the Strict profile when appropriate.

## Reference(s):

- [OOXML Lookup on ClawHub](https://clawhub.ai/shbernal/skills/ooxml-lookup)
- [Version 0.0.5 release notes](https://github.com/shbernal/ooxml-ai-tooling/releases/tag/v0.0.5)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Text and structured JSON lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local schema lookup defaults to Transitional; search and SQL results are capped at 200 rows.]

## Skill Version(s):

0.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
