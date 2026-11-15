## Description:

Summarize creates concise summaries and keyword lists from pasted text, local documents, and web pages with configurable output length.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to summarize long text, supported local documents, and web pages, and to extract keywords in text, Markdown, or JSON formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read user-specified local files.

Mitigation: Avoid using it with secret files or sensitive local documents unless the environment has appropriate file access controls.

Risk: The skill can fetch user-specified URLs without safeguards.

Mitigation: Avoid private or internal URLs, credential-bearing URLs, and sensitive network environments unless URL validation or network egress controls are added.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/summarize)
- [Publisher profile](https://clawhub.ai/user/paudyyin)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Plain text, Markdown, or JSON summaries and keyword lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports configurable summary length, keyword count, and optional metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
