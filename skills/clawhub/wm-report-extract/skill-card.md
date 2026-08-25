## Description:

Extracts traceable values, tables, and narrative evidence from A-share and Hong Kong IFRS financial-report PDFs through local conversion, table materialization, QA gates, and independent review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deadkingyy](https://clawhub.ai/user/deadkingyy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to extract specific fields or full structured datasets from financial-report PDFs, with page and quote provenance for downstream review. It is intended for report-driven workflows where local cache artifacts, quality checks, and independent review records are part of the extraction handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded PDFs, local report files, and optional symbol-mode lookups can introduce untrusted input or external service exposure.

Mitigation: Use trusted report URLs or local PDFs, understand optional WinMale service use before symbol mode, and run processing in a dedicated environment.

Risk: Extracted financial values can be misleading if conversion, table typing, quote verification, or QA review is incomplete.

Mitigation: Review generated quality.json and review.json before relying on extracted numbers, and consume only reviewed pass outputs where applicable.

Risk: The skill writes cache and result artifacts locally, including extracted report content.

Mitigation: Keep WM_REPORT_CACHE_DIR pointed at a dedicated cache directory and review cache cleanup commands before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deadkingyy/skills/wm-report-extract)
- [README](artifact/README.md)
- [Workflow reference](artifact/references/workflow.md)
- [Provenance contract reference](artifact/references/provenance.md)
- [Coverage checklist](artifact/references/coverage-checklist.md)
- [Open WinMale platform](https://open.winmale.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown guidance with bash commands and JSON, Markdown, and optional HTML result artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local cache and result artifacts such as manifest.json, quality.json, review.json, tables/*.json, fields/*.json, narratives/*.json, gaps.json, and report.md; downstream use should rely on reviewed outputs.]

## Skill Version(s):

0.6.1 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
