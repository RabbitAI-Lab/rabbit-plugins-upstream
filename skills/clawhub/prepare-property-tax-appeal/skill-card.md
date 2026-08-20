## Description:

Triage US residential real-property assessment review or appeal requests and prepare evidence packets when market value is a material ground.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mushanyoung](https://clawhub.ai/user/mushanyoung)

### License/Terms of Use:

MIT-0

## Use Case:

External property owners or their agents use this skill to classify US residential assessment disputes, verify filing routes and deadlines, analyze comparable sales, and prepare fact-checked appeal packet materials when market value is a material ground.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill processes sensitive property appeal facts and may reference private owner documents.

Mitigation: Use a fresh case directory, keep private documents separate from shared case data, and avoid storing credentials, private links, signed URLs, or unnecessary personal details.

Risk: Generated appeal statements can be incorrect if source facts, deadlines, or valuation rules are not current and verified.

Mitigation: Review every generated statement against official sources and owner-provided evidence before filing.

Risk: Using overwrite behavior can replace existing local output files.

Mitigation: Avoid force-overwrite options unless the existing Markdown and PDF outputs have been manually confirmed to belong to the same case.

Risk: PDF generation is limited to supported English/WinAnsi characters.

Mitigation: Use official English spellings for PDF output, or generate Markdown only when the case text includes unsupported characters.

## Reference(s):

- [Property Tax Appeal Methodology](references/methodology.md)
- [US Property Tax Appeal Routes](references/appeal-routes.md)
- [Case Data Schema](references/case-schema.md)
- [US Jurisdictions Routing Data](references/us-jurisdictions.json)
- [ClawHub skill page](https://clawhub.ai/mushanyoung/skills/prepare-property-tax-appeal)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance, structured JSON case data, and generated Markdown/PDF appeal packet files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow requires current official-source verification and human review before filing.]

## Skill Version(s):

3.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
