## Description:

Helps users draft, revise, review, and format Chinese official documents, workplace materials, and news copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Staff in government, businesses, schools, and news organizations use this skill to prepare Chinese official documents and work materials from supplied source information, improve existing drafts, check document structure and wording, and organize Word content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DOCX files can contain comments or hidden text that may be included in processing.

Mitigation: Provide only documents intended for processing, inspect comments and hidden text, and verify generated facts before sharing official documents.

Risk: Word editing and web research depend on host tools whose permissions may not be verified.

Mitigation: Confirm the host tools and their permissions are available for the requested task, and review sourced information before relying on it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [Source code and feedback](https://github.com/gongyu0918-debug/chinese-official-writing-skill)
- [Official document handling regulation reference](https://news.12371.cn/2013/02/22/ARTI1361522182793487_all.shtml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Writing guidance]

**Output Format:** [Chinese prose or Markdown; Word document formatting depends on available host tools.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the requested document type, supplied material, and editing scope.]

## Skill Version(s):

2.0.52 (source: server release metadata, README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
