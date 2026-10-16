## Description:

Generates a nested table of contents from headings in a user-provided Markdown file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation authors use this skill to preview a nested table of contents for a README or other long Markdown document before approving any write-back.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent reads the Markdown file supplied by the user, which may contain sensitive content.

Mitigation: Provide only a file the agent is permitted to read.

Risk: Writing a generated TOC back to the document could change its contents.

Mitigation: Review the preview and explicitly approve any later write-back.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/hmahmadcs/skills/markdown-toc-generator)

## Skill Output:

**Output Type(s):** [Markdown]

**Output Format:** [Markdown table of contents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Nested links to headings; printed as a preview without automatically changing the source file.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
