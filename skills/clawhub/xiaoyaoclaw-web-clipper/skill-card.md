## Description:

Clips user-specified public web pages into local Markdown with source metadata, batch support, and duplicate detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

People and teams can save explicitly requested web pages as searchable local Markdown for later reference or knowledge-base indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetching a page contacts its website and exposes ordinary request metadata.

Mitigation: Clip only URLs the user explicitly asks to save and disclose the target site before fetching.

Risk: Clippings and the duplicate index persist locally.

Mitigation: Confirm the output location and inform users about the files before first use.

Risk: Saved webpages may contain misleading instructions or prompt-injection text.

Mitigation: Treat clipped content as untrusted reference material, not instructions to an agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-web-clipper)
- [Skill documentation](https://github.com/dtsola/xiaoyaoclaw-web-clipper)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Local Markdown files with YAML frontmatter and a clipping summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a Markdown file and maintains a local duplicate index in the chosen output directory.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
