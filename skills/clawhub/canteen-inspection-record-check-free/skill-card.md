## Description:

A local Chinese-language checker for canteen purchase-inspection and food-sample retention records that runs six deterministic checks and cites source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

School, enterprise, and government canteen administrators use this skill to check purchase-inspection and food-sample retention records before monthly self-checks or regulatory reviews. It identifies arithmetic mismatches, missing meal-sample entries, low sample weights, duplicate supplier-batch rows, and missing or unparseable required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version does not perform several fuller compliance checks, including 48-hour retention, certificate validity, shelf-life checks, and disinfection gap detection.

Mitigation: Review the disclosed withheld checks and use an additional compliance review when those controls are required.

Risk: The skill checks provided record text and does not verify real-world food safety conditions, sample existence, document authenticity, original files, or regulator conclusions.

Mitigation: Treat findings as record-review support and keep human inspection, document verification, and regulatory review in the workflow.

Risk: When required columns or usable input are missing, the skill reports insufficient input rather than a pass or fail conclusion.

Mitigation: Provide a table with the required headers and rerun the checker before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/canteen-inspection-record-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON findings with cited source rows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes executed checks, withheld checks, insufficient-input messages, and local-processing status.]

## Skill Version(s):

1.0.6 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
