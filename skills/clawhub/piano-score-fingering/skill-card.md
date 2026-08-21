## Description:

Reads piano scores from images, PDFs, MusicXML, MXL, or MuseScore files, verifies score facts, generates playable two-hand fingering, and delivers annotated PDF or fingered MusicXML outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yannxinn](https://clawhub.ai/user/yannxinn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, music educators, pianists, and score-preparation users can use this skill to convert verified piano score facts into reviewable two-hand fingering plans, annotated PDFs, fingered MusicXML, and delivery reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-supplied score files and writes output PDFs, MusicXML, JSON plans, reports, and temporary files on the local machine.

Mitigation: Install only when local file access for provided scores and generated outputs is acceptable, and review generated artifacts before use.

Risk: Input PDFs are preserved and overlaid, so untrusted PDFs may carry document-level risk outside the skill's fingering workflow.

Mitigation: Use trusted input PDFs where possible and inspect resulting annotated outputs before sharing.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/Yannxinn/piano-score-fingering)
- [ClawHub skill page](https://clawhub.ai/yannxinn/skills/piano-score-fingering)
- [Professional Fingering Rules](references/professional-fingering-rules.md)
- [Unified Fingering Plan Schema](references/fingering-plan-schema.md)
- [Common Fingering Errors](references/common-fingering-errors.md)
- [PianoPlayer](https://github.com/marcomusy/pianoplayer)
- [pypdf](https://github.com/py-pdf/pypdf)
- [Ergonomic Model of Keyboard Fingering for Melodic Fragments](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/parncutt_richard/Pdfs/PaSlClRaDe97_FingeringModel.pdf)
- [A Simple Algorithm for Automatic Generation of Polyphonic Piano Fingerings](https://archives.ismir.net/ismir2007/paper/000355.pdf)
- [Merged-output HMM for Piano Fingering of Both Hands](https://eita-nakamura.github.io/articles/Nakamura_etal_MergedOutputHMMForPianoFingering_ISMIR2014.pdf)
- [Statistical Learning and Estimation of Piano Fingering](https://arxiv.org/pdf/1904.10237)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON plans, MusicXML, annotated PDF, PNG previews, and report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file outputs may include fingering-plan JSON, fingered MusicXML, annotated PDFs, preview images, anchor audits, review manifests, and delivery reports.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
