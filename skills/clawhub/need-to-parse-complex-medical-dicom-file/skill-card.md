## Description:

This skill provides offline, standard-library Python tools for DICOM metadata parsing, uncompressed pixel export, consistency checks, limited de-identification, and synthetic test-file generation, while refusing to decode compressed pixel data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical imaging teams use this skill to inspect .dcm files, extract DICOM metadata, export uncompressed pixels for visual checks, run basic consistency checks, perform limited PHI scrubbing, and generate synthetic DICOM fixtures. It is for technical inspection only, not clinical diagnosis or proof that de-identified files are safe to publish, upload, or share.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: De-identification may leave patient data in DICOM attributes or burned-in pixel annotations while users believe files are safe to share.

Mitigation: Keep outputs in a PHI-controlled environment and use a validated DICOM de-identification workflow plus independent review before publishing, uploading, or sharing files.

Risk: The tool is for technical inspection and does not support clinical diagnosis or regulatory compliance certification.

Mitigation: Use outputs only for engineering inspection and route diagnostic or compliance decisions to qualified clinical and regulatory workflows.

Risk: Compressed pixel data is not decoded by the bundled tools.

Mitigation: Treat compressed-pixel output as structural metadata only and use validated external decoders when pixel values are required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/orionshaowswmw/skills/need-to-parse-complex-medical-dicom-file)
- [DICOM file structure quick reference](artifact/references/dicom_basics.md)
- [DICOM de-identification design notes](artifact/references/ps315_deid.md)
- [DICOM transfer syntax quick reference](artifact/references/transfer_syntaxes.md)
- [DICOM PS3.5: Data Structures and Encoding](https://dicom.nema.org/medical/dicom/current/output/html/part05.html)
- [DICOM PS3.15: Security and System Management Profiles](https://dicom.nema.org/medical/dicom/current/output/html/part15.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or file outputs from bundled CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands emit JSON on stdout or stderr and may write PNM or DICOM files; bundled behavior is offline and deterministic.]

## Skill Version(s):

2.0.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
