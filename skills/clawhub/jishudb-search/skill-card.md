## Description:

Search existing JishuDB documents, list files, read text, and check import status; answer with source citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search an authorized JishuDB knowledge base, inspect existing document inventory or text, and answer questions from retrieved evidence with source filenames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An untrusted JISHUDB_URL or over-scoped JISHUDB_TOKEN could expose knowledge-base content to an unintended backend.

Mitigation: Install only where JISHUDB_URL points to a trusted JishuDB backend and scope any JISHUDB_TOKEN appropriately.

Risk: Search passages may be incomplete or low relevance, which can lead to unsupported answers if treated as full documents.

Mitigation: Answer only from observed tool output, cite source filenames, use document-reading tools for full text, and disclose when results cannot be verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/jishudb-search)
- [JishuDB skill homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown answers with source citations and optional Bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only knowledge-base queries; cites source filenames and reports unavailable tools or no matches.]

## Skill Version(s):

0.1.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
