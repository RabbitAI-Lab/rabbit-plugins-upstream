## Description:

Convert parcel boundaries into OvitalMap-compatible CSV files, assign stable parcel codes, and maintain deduplicated country and master archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeromeex](https://clawhub.ai/user/jeromeex)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and field-mapping teams use this skill to convert confirmed parcel coordinates into OvitalMap CSV exports, allocate stable parcel codes, and maintain local country and master archives. It supports WGS84, DMS, and UTM coordinate inputs, including archive re-exports and coordinate corrections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parcel coordinates and provider metadata are written to local CSV exports and archives.

Mitigation: Set OVITALMAP_WORKSPACE to a dedicated directory and manage access to the generated files according to the sensitivity of the parcel data.

Risk: Incorrect coordinates, country codes, provider names, or generated parcel codes could produce misleading map exports.

Mitigation: Review displayed WGS84 coordinates and proposed parcel codes before approval, and stop on needs_input or blocked responses until the requested fields are resolved.

Risk: The output may be mistaken for legal cadastral validation.

Mitigation: Use the generated files as mapping and export assistance only, not as cadastral or legal validation.

## Reference(s):

- [CSV Compatibility Contract](references/csv-contract.md)
- [Workflow Contract](references/workflow-contract.md)
- [Interaction and Edge Cases](references/interaction-and-edge-cases.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated CSV file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated exports and archives are local CSV files; OVITALMAP_WORKSPACE can set a dedicated output directory.]

## Skill Version(s):

3.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
