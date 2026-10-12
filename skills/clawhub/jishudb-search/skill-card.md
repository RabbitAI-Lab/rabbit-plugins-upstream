## Description:

Searches existing JishuDB knowledge bases to answer document questions with source citations, list available material, and check import status when the corresponding connection is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and other authorized users search existing internal knowledge bases, identify documents, read their contents, and check import progress using retrieved evidence rather than guesses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to the configured knowledge-base service.

Mitigation: Use only an authorized JishuDB endpoint and token, and avoid sending unrelated or sensitive queries to the wrong service.

Risk: Passage search cannot establish an exact file inventory or full document contents.

Mitigation: Use the connected document tools for inventories and full text; cite retrieved sources and disclose access or evidence gaps.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/jishudb-search)
- [Project homepage (listed in skill metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb-search)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with source filenames, or an access/status notice]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are based on retrieved results; full inventories and job status require the corresponding connected host tools.]

## Skill Version(s):

0.1.4 (source: ClawHub release; bundled frontmatter: 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
