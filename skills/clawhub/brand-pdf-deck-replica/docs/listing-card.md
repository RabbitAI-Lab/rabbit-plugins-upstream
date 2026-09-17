## Description:

Replicates a brand PDF report (BlackRock Investment Institute, McKinsey, Morgan Stanley style, typically exported from PowerPoint) into a same-size `pptx` + `pdf` + `html` triple, and reverse-engineers every chart's numbers out of the vector artwork into CSV.

It works by treating the PDF as a geometric source rather than a picture: vector paths give the series, and tick-label text coordinates (Latin characters survive even when CJK does not) give the calibration. Three independent methods cross-validate every value.

This skill is for research and development only.

## Publisher:

[yjkj999999](https://clawhub.ai/user/yjkj999999)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they receive an institutional PDF report and need either (a) a faithful, same-page-size deck they can reuse in their own reporting, or (b) the underlying chart data as CSV instead of eyeballing values off a rendered image. Typical scenarios: rebuilding a research deck in a corporate template, extracting historical series from a chart-only PDF, or verifying whether a vendor's chart is reproducible from its own PDF.

It is framed as engineering and research tooling. It does not generate investment advice, and replicated third-party reports remain subject to the original publisher's copyright and compliance rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Replicating a third-party research report may raise copyright or compliance issues if redistributed externally.

Mitigation: Confirm redistribution rights with the report publisher before sharing. Attribution and a clear note on the reconstruction method are recommended; the skill only produces layout and data artifacts locally.

Risk: When the source PDF's CJK glyphs lack a ToUnicode mapping, `pdftotext` returns garbage and text must be reconstructed from rendered images plus domain knowledge, so wording is not guaranteed to be verbatim.

Mitigation: The skill requires the operator to disclose that text was reconstructed and forbids presenting it as a verbatim reproduction. Verify wording against the original before external use.

Risk: Some pages may be tinted-mask bitmaps rather than vector artwork, making exact vector reconstruction impossible.

Mitigation: Probe each page first (`scripts/probe_pdf.sh`); declare the limitation explicitly and reproduce such areas as decorative reconstruction only, never as pixel-accurate copies.

Risk: Image-backed PPTX slides are not text-editable.

Mitigation: Page text is written into speaker notes to remain searchable and copyable, and the skill instructs the operator to disclose this trade-off and offer a native-shape fallback deck on request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yjkj999999/skills/brand-pdf-deck-replica)
- [Publisher profile](https://clawhub.ai/user/yjkj999999)
- [Project homepage](https://github.com/yjkj999999/brand-pdf-deck-replica)
- [README](README.md)
- [BlackRock 2026 mid-year outlook replication case study](examples/blackrock_2026_case.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands plus generated HTML, PDF, PPTX decks and per-series CSV data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output page size matches the source PDF exactly (e.g. 792x594pt). CSV precision and calibration residuals are reported per chart; any chart whose residual exceeds the 0.1pt acceptance line is named explicitly rather than averaged away.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. When the source is a third-party research publication, the user is responsible for confirming that any reproduction or redistribution is permitted.
