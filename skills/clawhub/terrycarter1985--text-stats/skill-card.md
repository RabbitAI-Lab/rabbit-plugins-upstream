## Description:

Analyze text files to report word count, character count, sentences, paragraphs, reading time, and most frequent words with filtering options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, editors, and agents use this skill to summarize the size and structure of text or Markdown files, estimate reading time, and identify frequent non-stopword terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected text and Markdown files and prints text-derived summaries that may appear in terminal output or logs.

Mitigation: Use it only on files or directories whose derived statistics are acceptable to display in the terminal or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/text-stats)

## Skill Output:

**Output Type(s):** [analysis, text, json, shell commands, guidance]

**Output Format:** [Human-readable terminal report by default, with newline-delimited JSON objects when --json is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports file name, word count, raw and non-space character counts, sentence count, paragraph count, estimated reading time, and filtered top words.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
