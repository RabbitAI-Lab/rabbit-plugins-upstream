## Description:

Upload videos to Bilibili (哔哩哔哩). Supports automatic login, title, description, tags, and partition selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[izorro](https://clawhub.ai/user/izorro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content automation users use this skill to upload local video files to Bilibili with configurable titles, descriptions, tags, and partition IDs. It is useful for automating repeat uploads after the required interactive Bilibili login is completed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The biliup login flow creates local cookies that can keep the Bilibili account usable for future uploads.

Mitigation: Use a dedicated environment where possible, and revoke or remove the stored cookies when automated uploading is no longer needed.

Risk: The skill depends on the external biliup package to perform uploads.

Mitigation: Review and pin the biliup package before use, and avoid installing or running it with administrator privileges.

Risk: Running the skill uploads selected local videos to Bilibili from the current machine.

Mitigation: Use it only when you intend to publish the chosen video files, and review title, description, tags, and partition ID before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/izorro/skills/bilibili-upload)
- [ClawHub publisher profile](https://clawhub.ai/user/izorro)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and command-line status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local command-line execution and Bilibili account cookies created by biliup login.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
