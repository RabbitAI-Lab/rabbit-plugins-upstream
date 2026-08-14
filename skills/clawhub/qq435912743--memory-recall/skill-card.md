## Description:

Memory Recall helps agents search local Markdown and plain-text notes with keyword, tag, date, path, and recency-weighted retrieval, returning sourced snippets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve prior decisions, links, code snippets, and topic timelines from local note directories. The skill is intended for scoped personal-memory and note search where returned snippets should remain traceable to source files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The note search script can recursively read local Markdown and text files from directories supplied by the user.

Mitigation: Use a narrow notes directory, avoid folders that may contain secrets or unrelated personal data, and review returned snippets before sharing them.

Risk: The optional learner records usage, errors, notes, and preferences into persistent local state.

Mitigation: Enable the learner only when persistent local learning is desired, keep its skill directory scoped, and inspect or remove learned_patterns.json when the retained state is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/memory-recall)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output may include source paths, line numbers, snippets, scores, and matched-line counts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
