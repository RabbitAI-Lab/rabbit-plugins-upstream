## Description:

Fetches and parses Feishu (Lark) Wiki, Docs, Sheets, and Bitable content from URLs into Markdown, text, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and automation workflow users can use this skill to retrieve Feishu document, wiki, sheet, and Bitable content and convert it into agent-readable Markdown, text, or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read, write, and command execution capability may exceed what is needed for Feishu document retrieval.

Mitigation: Review before installing and prefer a version limited to explicit Feishu URL retrieval without generic command execution.

Risk: Feishu document content and access tokens may include sensitive workspace data.

Mitigation: Use least-privilege Feishu access, keep credentials out of shared outputs, and confirm privacy handling before processing sensitive documents.

Risk: The artifact describes unrelated messaging, file, and command features without clear controls.

Mitigation: Disable or avoid those features unless the deployment defines clear authorization, logging, and scope limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-doc)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown, plain text, or JSON with Feishu document metadata and extracted content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source URL, resolved URL, document type, title, block counts, sheet rows, or Bitable records when available.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
