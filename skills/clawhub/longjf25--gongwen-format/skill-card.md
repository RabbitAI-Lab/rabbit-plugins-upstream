## Description:

Creates Chinese official documents (gongwen) following GB/T 9704-2012 and common enterprise formatting requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longjf25](https://clawhub.ai/user/longjf25)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document authors use this skill to draft or generate Chinese official documents such as notices, reports, decisions, replies, letters, and minutes with GB/T 9704-style layout, fonts, margins, heading hierarchy, and attachment formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The JavaScript template depends on the docx package, so unpinned dependency installation can introduce supply-chain drift.

Mitigation: Use a pinned docx dependency and a lockfile before running the template.

Risk: Broad triggers may activate the skill for ordinary writing or report requests.

Mitigation: Invoke it only when GB/T 9704-style Chinese official document formatting is actually needed.

Risk: Running the bundled JavaScript template writes a .docx file to disk.

Mitigation: Review the output path and run the template only in an intended working directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/longjf25/skills/gongwen-format)
- [GB/T 9704-2012 summary](artifact/gb9704_2012.md)
- [docx-js gongwen template](artifact/gongwen_template.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with document formatting specifications, JavaScript docx template code, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May help adapt a docx-js template that writes a generated .docx file when the user runs the JavaScript.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
