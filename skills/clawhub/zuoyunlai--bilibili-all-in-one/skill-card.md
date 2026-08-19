## Description:

A comprehensive Bilibili toolkit that integrates hot trending monitoring, video downloading, video watching/playback, subtitle downloading, and video publishing capabilities into a single unified skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to monitor Bilibili trends, inspect video statistics, download videos or subtitles, retrieve playback data, and publish videos through Bilibili APIs. Most read-only features work without credentials, while publishing and high-quality downloads require Bilibili session cookies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing and high-quality downloads require Bilibili session cookies that can grant broad account access if mishandled.

Mitigation: Use a test account, provide cookies only when needed, and revoke or rotate the session after use.

Risk: Optional credential persistence writes session material to a local .credentials.json file.

Mitigation: Leave BILIBILI_PERSIST unset unless persistence is necessary, and delete .credentials.json when finished.

Risk: Pinned dependencies may become stale for long-running or serious deployments.

Mitigation: Install in an isolated virtual environment and review or update pinned dependencies before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/bilibili-all-in-one)
- [Publisher profile](https://clawhub.ai/user/zuoyunlai)
- [Project homepage from ClawHub metadata](https://github.com/wscats/bilibili-all-in-one)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, files]

**Output Format:** [JSON or text responses with optional downloaded media, subtitle, and metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI and Python API actions may call Bilibili endpoints and may write downloaded video, audio, subtitle, credential, or upload-related files depending on the action.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
