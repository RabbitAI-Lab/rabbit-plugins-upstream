## Description:

Analyze text files to report word count, character count, sentences, paragraphs, reading time, and most frequent words with filtering options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and editors use this skill to quickly inspect text or Markdown files for size, reading-time estimates, and frequent terms, including single-file and directory analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local text and Markdown files that the user asks it to analyze, so directory analysis can include private documents if a broad path is selected.

Mitigation: Run it only on intended files or narrow directories, and avoid broad private folders unless their contents are meant to be analyzed.

## Reference(s):

- [ClawHub Text Stats skill page](https://clawhub.ai/terrycarter1985/skills/text-stats)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text report or JSON records from the Python script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes local .txt and .md files; directory mode walks matching files recursively.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
