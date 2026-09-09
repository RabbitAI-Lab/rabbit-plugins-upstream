## Description:

Long Doc Translation guides agents through an end-to-end workflow for high-quality Chinese translation of long foreign-language scholarly works, from parsing and chunking through glossary setup, batch translation, QA, and merged Markdown/HTML delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External translators, researchers, and developers use this skill to coordinate full-book Chinese translation projects for long scholarly works while preserving terminology, page anchors, notes, QA findings, and merged reader deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad translation triggers may activate the skill for shorter translation requests where the full long-document workflow is unnecessary.

Mitigation: Confirm that the user wants a long-document or full-book workflow before applying the complete pipeline.

Risk: The boundary deduplication script can modify chunk files when run with --apply.

Mitigation: Run the script in dry-run mode first and review proposed removals before applying changes.

Risk: OCR artifacts, overlapping slices, or inconsistent terminology can propagate into a long merged translation.

Mitigation: Use the documented glossary, page-code retention, overlap checks, QA script, and translator notes before final merging.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and reusable Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate or validate chunked translation files, QA reports, merged Markdown manuscripts, and self-contained HTML reader output.]

## Skill Version(s):

1.1.0 (source: evidence release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
