## Description:

Publish and schedule videos, photo carousels, text posts, and documents across supported social platforms through Upload-Post API calls, with guidance for status checks, history, analytics, and media processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[victorcavero14](https://clawhub.ai/user/victorcavero14)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, and developers use this skill to let an agent prepare Upload-Post API calls for publishing, scheduling, checking status, reviewing history, retrieving analytics, and processing media across connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent delegated access to publish, schedule, edit, and cancel posts on connected social accounts.

Mitigation: Use a dedicated Upload-Post profile or limited connected accounts, and require explicit human confirmation before publishing, scheduling, editing, or canceling posts.

Risk: The Upload-Post API key enables broad account actions if exposed.

Mitigation: Use a revocable key, inject it only for this skill, and avoid placing the key in prompts, logs, shared files, or generated content.

Risk: The FFmpeg endpoint accepts a free-form full_command for remote media processing.

Mitigation: Require explicit approval before using full_command, inspect the command and media inputs, and avoid processing sensitive files unless necessary.

Risk: Cross-platform publishing can partially succeed, which may create inconsistent campaign state or duplicate posts on retry.

Mitigation: Poll status, report each platform result separately, retry only failed platforms, and use idempotency keys for retryable requests.

## Reference(s):

- [Upload-Post homepage](https://upload-post.com)
- [Upload-Post API documentation](https://docs.upload-post.com)
- [Upload-Post LLM-friendly documentation](https://docs.upload-post.com/llm.txt)
- [Platform-Specific Parameters](references/platforms.md)
- [Media Requirements by Platform](references/requirements.md)
- [ClawHub skill page](https://clawhub.ai/victorcavero14/skills/upload-post)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and UPLOAD_POST_API_KEY; outputs may include API calls for publishing, scheduling, editing, canceling, status checks, analytics, and media processing.]

## Skill Version(s):

1.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
