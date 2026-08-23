## Description:

Turn user-uploaded files and conversation into a durable, versioned meeting charter that can be retrieved or updated later, and create a one-time pre-meeting reminder that reloads the latest charter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metaphor279](https://clawhub.ai/user/metaphor279)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and meeting organizers use this skill to prepare, save, review, revise, and retrieve Tencent Meeting charters from uploaded files, user conversation, and selected meeting metadata. When explicitly requested, it creates a one-time pre-meeting reminder that reloads the latest saved charter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting materials may contain sensitive information and the skill can save charter markdown files in the current workspace.

Mitigation: Use the skill only in workspaces authorized for the meeting content and avoid highly sensitive materials unless that storage location is approved.

Risk: A charter may become misleading if conflicting sources or multiple matching meetings are resolved incorrectly.

Mitigation: Confirm meeting selections, mark unresolved conflicts as pending confirmation, and preserve confirmed decisions when updating saved charters.

Risk: A pre-meeting reminder may not be created if the host agent lacks one-time scheduling capability.

Mitigation: Create reminders only after explicit user request and a saved charter; if scheduling is unavailable, return the trigger specification and state that no active reminder was created.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown meeting charter with YAML front matter, saved file paths, version details, pending-confirmation notes, and optional reminder trigger details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charters are saved under the current workspace meeting-charters directory when the user asks to save, retrieve, update, or create a reminder.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
