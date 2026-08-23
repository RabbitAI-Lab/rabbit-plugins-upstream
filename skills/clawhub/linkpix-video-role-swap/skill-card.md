## Description:

LinkPix video role replacement uses qhkit to replace a person in an original video with a supplied character image while preserving the source motion and lip movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare localized or replacement-character videos from an original video, one authorized character image, and the video's duration. It is intended for video role replacement, face/model replacement, digital human replacement, and model localization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if users paste credentials into chat.

Mitigation: Configure credentials through local files, environment variables, or platform secret mechanisms instead of sharing raw keys in conversation.

Risk: Video and likeness replacement can misuse a person's image or identity.

Mitigation: Use only videos and likenesses the user is authorized to process, confirm authorization before task submission, and refuse unauthorized face or role replacement requests.

Risk: Media files are uploaded to the provider during qhkit processing.

Mitigation: Tell users that provider-side upload and processing are expected, and avoid submitting sensitive media unless the user has permission and accepts that handling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-video-role-swap)
- [qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status guidance, credit information, and video delivery URLs after execution.]

## Skill Version(s):

0.1.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
