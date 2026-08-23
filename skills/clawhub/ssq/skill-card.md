## Description:

Parses architectural drawings in DWG, DXF, PDF, and image formats and extracts structured text, paragraphs, material tables, dimensions, layers, and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yfg305](https://clawhub.ai/user/yfg305)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and review teams use this skill to convert building drawings into structured local JSON outputs for planning, extraction, and audit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned or optional OCR and CAD dependencies may change behavior across installs.

Mitigation: Pin dependency versions for production use and review optional OCR and CAD tools before installing them.

Risk: The skill should run only for intended technical drawing parsing workflows.

Mitigation: Invoke it with explicit CAD, PDF, or building-drawing language and route unrelated files to other tooling.

Risk: Parsed drawing outputs are written to local extraction files.

Mitigation: Choose an appropriate output directory and review generated JSON before using it in planning or audit decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yfg305/skills/ssq)
- [Server-resolved GitHub provenance](https://github.com/yfg305/ssq)
- [PyMuPDF documentation](https://pymupdf.readthedocs.io/)
- [ezdxf project](https://github.com/mozman/ezdxf)
- [RapidOCR project](https://github.com/RapidAI/RapidOCR)
- [Open Design Alliance File Converter](https://www.opendesign.com/guestfiles/oda_file_converter)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, files]

**Output Format:** [JSON files, Python return dictionaries, and concise command-line status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local extraction results under the configured output directory, including _drawing_parser/project_data.json.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
