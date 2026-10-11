## Description:

Creates or repairs editable PowerPoint presentations with slide copy, speaker notes, and sourced claims for work updates, proposals, and knowledge sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and other presentation authors use this skill to finish or improve an editable slide deck from a topic or unfinished presentation, with speaker notes and citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install and launch JishuDB Desktop or modify a local agent connection.

Mitigation: Review the proposed release, destination paths, and client configuration changes before approving setup.

Risk: Presentation sources and drafts may be retained in a knowledge base, and public research could expose confidential material if mishandled.

Mitigation: Approve the knowledge-base destination and write scope; avoid confidential work unless retention and search behavior are acceptable.

Risk: The skill creates local presentation and Markdown files.

Mitigation: Confirm output paths and review generated files before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/ppt-rescue-kit)
- [Project homepage (skill metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/ppt-rescue-kit)
- [Bundled JishuDB setup guide](artifact/references/jishudb-setup/setup.md)
- [Bundled task execution defaults](artifact/references/jishudb-setup/task-execution.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Text]

**Output Format:** [Editable PPTX with Markdown slide copy, speaker notes, sources, and revision notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires approved knowledge-base retention of presentation records; reports incomplete work when required output or retention fails.]

## Skill Version(s):

0.1.7 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
