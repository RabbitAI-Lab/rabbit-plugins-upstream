## Description:

Removes unwanted text and watermarks from user-selected images, hard subtitles and visible watermarks from videos, and platform watermarks from supported video share links using the 550W service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sunshinehu](https://clawhub.ai/user/sunshinehu)

### License/Terms of Use:

MIT-0

## Use Case:

People and content creators use this skill to remove text, subtitles, or watermarks from media they own or are authorized to process, or to obtain watermark-free video links from supported public share links. It connects through OAuth or an API key and may consume account credits.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Selected media or links are sent to the 550W service.

Mitigation: Grant access only to media explicitly selected by the user and confirm the file or link before uploading.

Risk: API keys may be stored in the local user configuration directory.

Mitigation: Prefer OAuth when supported; protect locally stored credentials and never disclose them in messages or logs.

Risk: Processing can spend account credits, and task deletion removes a selected task.

Mitigation: Confirm the account and selected item before paid processing, and obtain separate confirmation before deleting a task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sunshinehu/skills/550w-ai-media-cn)
- [OAuth access guide](references/oauth-access.md)
- [API key access guide](references/openapi-access.md)
- [API contract](references/api-contract.md)
- [Agent compatibility](references/agent-compatibility.md)

## Skill Output:

**Output Type(s):** [Text, Links, Guidance]

**Output Format:** [Text with result URLs and task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID for later status checks or a direct link to processed media.]

## Skill Version(s):

3.1.3 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
