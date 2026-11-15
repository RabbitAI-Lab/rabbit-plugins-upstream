## Description:

Supports agent workflows for creating, editing, analyzing, cleaning, and converting spreadsheet files, with guidance for formulas, formatting, recalculation, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisz112](https://clawhub.ai/user/lisz112)

### License/Terms of Use:

Proprietary Anthropic Terms

## Use Case:

Developers and spreadsheet-focused agents use this skill when a user needs a spreadsheet file created, repaired, cleaned, analyzed, formatted, converted, or updated while preserving formulas and workbook conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local LibreOffice and adds a persistent recalculation macro to the LibreOffice user profile.

Mitigation: Install and run it in an isolated workspace or LibreOffice profile, then review and remove the profile macro when it is no longer needed.

Risk: The skill includes a native LD_PRELOAD workaround for restricted LibreOffice environments.

Mitigation: Review the workaround before installation and avoid using it outside isolated environments that require it.

Risk: The release includes Word and PowerPoint document tooling beyond the spreadsheet-centered skill description.

Mitigation: Remove or split the DOCX/PPTX helpers if the approved deployment scope is limited to spreadsheet handling.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Files, Configuration instructions]

**Output Format:** [Markdown guidance with Python and shell snippets; spreadsheet files and JSON validation output from bundled utilities]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects spreadsheet deliverables to be recalculated and checked for formula errors when formulas are used.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
