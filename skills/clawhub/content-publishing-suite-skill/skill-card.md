## Description:

This skill turns a fact-checked and compliance-approved final Markdown draft into multi-channel publishing assets: WeChat article HTML, a WeChat image-summary card and copy, a LinkedIn post, a standalone responsive HTML page, and a local archive ledger with optional Notion entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, editors, and publishing engineers use this skill to package an already reviewed final Markdown draft for WeChat, LinkedIn, standalone HTML, and archive workflows. It is intended for publishing orchestration and format conversion, not for fact-checking, writing, or automatic external posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can generate and update local publishing files, including an archive ledger, from approved drafts.

Mitigation: Run it only on intentionally selected final drafts and review the generated package, ledger entry, and manifest before publication.

Risk: The skill is not a fact-checker and can propagate errors if the input draft was not already reviewed.

Mitigation: Require the documented approval gate, such as an approved final-check file or explicit reviewed marker, before generating publishing assets.

Risk: External publishing or Notion archiving could publish or persist content outside the local workspace.

Mitigation: Keep external actions in dry-run mode unless the user explicitly confirms targets, and provide credentials only when confirmed publishing or archiving is intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/content-publishing-suite-skill)
- [WeChat Style Reference](references/wechat-style.md)
- [Channel Contracts](references/channel-contracts.md)
- [WeChat Snippet Template](templates/wechat-snippet.html)
- [LinkedIn Post Template](templates/linkedin-post.md)
- [Standalone HTML Template](templates/standalone.html)
- [Archive Record Template](templates/archive-record.json)
- [Notion Mapping Example](templates/notion-mapping.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, HTML, JSON, shell commands, and publishing package files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local publishing assets and gate reports; external publishing or Notion writes require explicit user confirmation.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
