## Description:

Guides an agent through detecting, parsing, and verifying complex medical DICOM files when standard tooling is insufficient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to structure DICOM parsing tasks, select local DICOM tooling, and verify extracted outputs. It is not intended for diagnosis and should be used only with medical imaging files the user is authorized to process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Medical imaging inputs and outputs may contain protected health information.

Mitigation: Process only authorized DICOM files and protect generated outputs and logs according to applicable medical-data policies.

Risk: DICOM parsing guidance may be incomplete or incorrect for complex cases and is not diagnostic.

Mitigation: Validate results with qualified DICOM tooling and appropriate professional review before relying on them.

Risk: Optional dependency installation may require network access.

Mitigation: Install dependencies from approved sources in a controlled environment and avoid unnecessary network access when processing medical data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/need-to-parse-complex-medical-dicom-file)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
