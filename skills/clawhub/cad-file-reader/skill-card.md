## Description:

Extract structured data from DWG, DXF, DWT and PDF drawings: text, layers, blocks, geometry, coordinates, annotations, tables, points, areas and design notes. Results include readable summaries, review-ready tables, source evidence and JSON. Outputs are review candidates with final_quantity=false, not final quantities or settlement data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Developers, CAD technicians, and design reviewers use this skill to extract text, layers, geometry, coordinates, annotations, tables, and measurement candidates from DWG, DXF, DWT, and PDF drawings into review-ready summaries and JSON. The results preserve source evidence for review and are not final quantities, settlement values, or compliance conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF processing may use a vulnerable pdfminer.six version.

Mitigation: Before processing PDFs, verify that the execution environment uses pdfminer.six 20251230 or newer.

Risk: An invalid page selection can cause the whole PDF to be processed.

Mitigation: Check page selections, work from a copy, and review the extracted evidence and report before sharing results.

Risk: Setup can download dependencies, and release-scrub can modify files when applied.

Mitigation: Preview Linux installation or use SKIP_APT=1; set CAD_AUTO_SETUP=0 to disable automatic dependency downloads. Back up customized vendor files and avoid release-scrub --apply on important originals.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Readable summaries and review-ready tables with source evidence, plus JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are review candidates with final_quantity=false; they are not final quantities or settlement data.]

## Skill Version(s):

0.39.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
