## Description:

QQ群作业整理 helps an agent fetch QQ group homework for a chosen date, preserve text and image attachments, format it into A4 Word or PDF documents, and optionally send the result by email or WeCom after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laneovcc](https://clawhub.ai/user/laneovcc)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as caregivers, students, or educators use this skill to collect QQ group homework from one or more groups, filter it by date or subject, and generate a printable homework document. It can also help send the generated document after recipient and attachment confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates a logged-in QQ browser outside the sandbox.

Mitigation: Use a dedicated or disposable browser profile when possible and install only after accepting this access model.

Risk: Homework exports may contain sensitive class, student, or family information.

Mitigation: Review qq_hw.json and generated documents before use, and prefer text-only mode for sensitive classes when images are unnecessary.

Risk: Sending generated documents can expose data to the wrong recipient or with the wrong attachment.

Mitigation: Confirm every recipient, subject, and attachment before any email or WeCom send.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/laneovcc/skills/qq-group-homework-summarizer)
- [QQ homework API reference](references/api.md)
- [Troubleshooting and reverse-engineering notes](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with command examples; generated JSON, DOCX, and PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create qq_hw.json, hw_list.json, hw_day_<date>.json, 作业_<date>.docx, and 作业_<date>.pdf; email or WeCom sending requires explicit user confirmation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
