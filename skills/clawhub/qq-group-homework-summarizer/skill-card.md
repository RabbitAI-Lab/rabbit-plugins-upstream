## Description:

从 QQ 群作业中抓取指定日期的文字和图片附件，生成排版规范的 A4 Word/PDF 作业文档，并可在授权后通过邮箱或企业微信发送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[laneovcc](https://clawhub.ai/user/laneovcc)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and family education workflows can use this skill to collect QQ group homework for a selected date, preserve images, format it into printable documents, and send the result to an approved destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a logged-in QQ browser session and may access private group, student, teacher, homework, and attachment information.

Mitigation: Confirm the QQ group and date before running, use only an intended logged-in account, and protect or delete qq_hw.json plus generated homework files after use.

Risk: The skill creates local documents and can send homework files through mail or WeCom when authorized.

Mitigation: Confirm the destination and attachment before sending, require explicit authorization for delivery, and avoid writing success markers unless delivery is actually confirmed.

Risk: The artifact invokes browser automation and Word/PowerShell helpers for PDF conversion and page checks, which depend on local environment state.

Mitigation: Run the built-in doctor check first, review proposed shell commands before execution, and install or upgrade dependencies only from trusted package sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/laneovcc/skills/qq-group-homework-summarizer)
- [QQ group homework API reference](artifact/references/api.md)
- [Troubleshooting and operations notes](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local JSON, DOCX, and PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create qq_hw.json, hw_list.json, hw_day_<date>.json, image cache files, Word documents, PDFs, page-count files, and sent markers in the working directory.]

## Skill Version(s):

1.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
