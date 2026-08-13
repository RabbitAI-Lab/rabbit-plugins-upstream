## Description:

Turns a reviewed, compliance-approved Markdown draft into WeChat, LinkedIn, standalone HTML, and archive-ledger publishing assets without repeating fact-checking or automatically publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external content teams, and developers use this skill to package an already reviewed Markdown draft into platform-specific publishing assets, local previews, and an archive ledger. It is intended for generate-only publishing preparation unless the user explicitly confirms an external write target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreviewed or newly changed draft content could be packaged as if it were ready for publication.

Mitigation: Require the documented input approval gate before packaging and roll back any newly introduced facts for upstream verification.

Risk: Optional platform or Notion writes could publish or archive externally before the user intends.

Mitigation: Keep generate-only dry-run behavior by default, list exact external targets, obtain explicit user confirmation, and read back after writing.

Risk: Publishing assets could leak internal notes, process traces, pen names, or credentials.

Mitigation: Apply the channel contracts and output gate checks that block conversation traces, internal notes, configured pen names, and credential-like tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/content-publishing-suite-skill)
- [WeChat inline style reference](references/wechat-style.md)
- [Channel output contracts](references/channel-contracts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated HTML, Markdown, JSON, and manifest file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local publishing assets only by default; external writes require explicit user confirmation and readback verification.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
