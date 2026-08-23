## Description:

Converts PDFs, Office documents, spreadsheets, slides, web and data files, images, audio, archives, YouTube links, and EPUBs into cleaned Markdown for RAG workflows using MarkItDown with local fallback converters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-engineering teams use this skill to convert mixed document collections into cleaned Markdown for RAG ingestion, knowledge-base preparation, and repeatable batch conversion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal use can install packages and modify the local Python or uv tool environment.

Mitigation: Use the skill only where automatic PyPI or uv installation is acceptable, or preinstall and review dependencies before running conversions.

Risk: Untrusted documents may carry parser or content risks during conversion.

Mitigation: Convert untrusted documents only in a sandboxed workspace with limited filesystem access.

Risk: Output files or cleaned Markdown can be overwritten during conversion or post-cleaning.

Mitigation: Confirm output paths before execution and prefer explicit new output paths for post_clean.py.

Risk: Batch conversion can recursively process large source trees and write many output files.

Mitigation: Confirm the source directory, output directory, file count, and extension filters before starting batch work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ebandao777-oss/skills/make-to-markdown)
- [Server-Resolved GitHub Source](https://github.com/ebandao777-oss/make-to-markdown)
- [README.md](artifact/README.md)
- [QUICKSTART.md](artifact/QUICKSTART.md)
- [REFERENCE.md](artifact/REFERENCE.md)
- [uv Documentation](https://docs.astral.sh/uv/)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files with concise conversion status summaries and command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write Markdown outputs and error logs; normal operation can install Python packages through pip or uv when dependencies are missing.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
