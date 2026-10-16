## Description:

Turns a user-provided EPUB or PDF book into an offline HTML reading report with a full-book summary, a card-based mind map, chapter summaries, and reviewable local intermediate files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bwgao](https://clawhub.ai/user/bwgao)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and researchers use this skill to turn a complete ebook into a structured, offline book report and chapter-by-chapter notes grounded in the supplied text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The output folder retains the source ebook and extracted chapters, which may contain copyrighted or private content.

Mitigation: Use books you are authorized to process; choose an approved local folder and review access before sharing the outputs.

Risk: Incorrect PDF chapter boundaries can distort or omit content from the final summary.

Mitigation: If PDF extraction falls back to heading detection, confirm the proposed chapter list and page ranges before summarization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bwgao/skills/book-breakdown)
- [Server-resolved source directory](https://github.com/bwgao/book-distill-skill/tree/main/book-breakdown-claude)
- [Chapter extraction guidance](references/extraction.md)
- [Offline HTML output guidance](references/html-output.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [Local Markdown and JSON files plus a self-contained offline HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local copy of the source ebook and extracted chapter text.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
