## Description:

Humanizer rewrites text to remove common signs of AI-generated writing while preserving meaning, tone, and readability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, editors, and other external users use this skill to revise drafts that sound AI-generated into more natural prose. It focuses on patterns such as inflated significance, vague attribution, promotional phrasing, repetitive structure, excessive hedging, and chatbot artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rewriting can accidentally change exact meaning or remove wording that matters in legal, policy, academic, quoted, or compliance-sensitive text.

Mitigation: Review the rewritten text or file diff before accepting changes, especially where precise wording matters.

Risk: The skill is intended for intentional rewriting tasks and can make authored or generated text harder to identify as AI-assisted.

Mitigation: Use it only where rewriting is appropriate and keep required authorship, disclosure, citation, and review processes intact.

## Reference(s):

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [Wikipedia: WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with rewritten content and optional change summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose edits to existing documents; users should review diffs before accepting changes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter and changelog mention 2.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
