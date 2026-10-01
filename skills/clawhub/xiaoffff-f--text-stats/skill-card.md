## Description:

Computes word count, character count, paragraph count, sentence count, and estimated reading time for provided text or text files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoffff-f](https://clawhub.ai/user/xiaoffff-f)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, editors, and other users can ask an agent to summarize basic text statistics for pasted text or a selected text file. The skill supports quick word-count, character-count, paragraph-count, sentence-count, and reading-time estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File mode reads the user-selected file contents to calculate text statistics.

Mitigation: Provide only files you are comfortable having read for this calculation.

Risk: Reading-time estimates are approximate and depend on simple Chinese and English rate assumptions.

Mitigation: Treat the reading time as a rough estimate, not an accessibility, editorial, or compliance measurement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoffff-f/skills/text-stats)
- [Server-resolved provenance unavailable](provenance:unavailable)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Concise Markdown report, optionally informed by JSON output from the bundled script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script emits JSON with counts for characters, non-space characters, CJK characters, Latin words, sentences, paragraphs, and estimated reading minutes.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
