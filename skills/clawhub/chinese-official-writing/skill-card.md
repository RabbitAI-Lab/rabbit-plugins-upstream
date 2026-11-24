## Description:

Helps users draft, revise, review, and format Chinese official documents, workplace materials, and news copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users in government, businesses, schools, and news organizations use it to prepare and review Chinese official documents and related materials, including Word files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign at medium confidence, but analysis of scripts/patch_docx.py is incomplete and effective file-reading permissions are unknown.

Mitigation: Review the script and the access granted to the skill before installation, and limit use to intended documents.

Risk: Drafts may be inaccurate when supplied facts are incomplete or conflict.

Mitigation: Check names, dates, figures, event status, and conclusions against the source material before issuing a document.

## Reference(s):

- [ClawHub release](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Chinese prose or Markdown, command-line output, Python code, and formatted DOCX files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include document review notes, formatting checks, or editing results based on supplied source material.]

## Skill Version(s):

2.1.4 (source: server-resolved release metadata, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
