## Description:

Counts characters, lines, and words, lists frequent terms, and estimates reading time for a file or directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code); All rights reserved (documentation and theory)

## Use Case:

Writers and developers can check text length, word frequency, and estimated reading time for individual files or batches of text files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests write and web access beyond what its local statistics script needs.

Mitigation: Review the package before installation; narrow permissions or run the script manually on selected files.

Risk: Documentation describes apply/write workflows that the statistics script does not provide.

Mitigation: Check the script's supported arguments before use and do not rely on the documented write safeguards.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/text-stats)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [File, character, word, and line counts; top terms and estimated reading time.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
