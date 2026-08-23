## Description:

Suji Board is a zero-dependency, single-file browser note board for collecting text snippets and images, organizing uploaded documents, setting reminders, and exporting structured notes as Word documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weijunz766-collab](https://clawhub.ai/user/weijunz766-collab)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to package or provide a local-first browser tool for collecting pasted text, images, reminders, and uploaded files, then organizing the material into a Word document. It is suited to note taking, research collection, report drafting, and lightweight document archiving workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The app can retain private notes, pasted clipboard content, images, reminders, and uploaded documents in browser local storage longer than users expect.

Mitigation: Avoid highly sensitive content on shared devices, and clear the site's localStorage and IndexedDB when the retained data is no longer needed.

Risk: The Check Update and Feedback actions contact ClawHub or Google Forms, which leaves the otherwise local-only workflow.

Mitigation: Disclose these external actions to users and avoid using them in workflows that require strictly offline or local-only operation.

## Reference(s):

- [Suji Board product introduction](references/product-intro.md)
- [ClawHub skill page](https://clawhub.ai/weijunz766-collab/skills/suji-board)

## Skill Output:

**Output Type(s):** [Guidance, Code, Files]

**Output Format:** [Markdown guidance and a single-file HTML application that can export .docx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The browser application stores notes, images, reminders, and uploaded files locally and includes manual update and feedback links.]

## Skill Version(s):

1.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
