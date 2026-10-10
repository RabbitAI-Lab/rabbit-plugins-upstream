## Description:

Searches authorized JishuDB knowledge bases and internal documents to answer questions, list files, read document text, and report import status using retrieved evidence and source citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized agents use this skill to find facts in existing JishuDB knowledge bases, inspect document inventories and contents, and check import status without importing new material or researching the public web.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries could be sent to an unintended knowledge-base service or disclose internal material.

Mitigation: Use only an authorized connection, confirm JISHUDB_URL points to the intended service, and prefer host-scoped read-only MCP tools.

Risk: The JISHUDB_TOKEN bearer credential could be exposed.

Mitigation: Protect the token as a secret and provide it only to the intended JishuDB connection.

Risk: Search snippets can be mistaken for a complete inventory or full document.

Mitigation: Cite retrieved passages for factual answers and use the appropriate live document tools for complete inventories or document text.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bowen-aijishu/skills/jishudb-search)
- [Skill metadata homepage (not verified provenance)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Source-cited natural-language answers and lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites retrieved source filenames; exact inventories and import status require the corresponding live host tools.]

## Skill Version(s):

0.1.3 (source: ClawHub release; artifact metadata reports 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
