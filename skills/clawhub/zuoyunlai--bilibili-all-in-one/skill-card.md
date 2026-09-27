## Description:

A comprehensive Bilibili toolkit that helps agents monitor trends, download videos, inspect playback and engagement data, manage subtitles, and prepare publishing workflows through CLI and Python interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor Bilibili trends, retrieve video metadata, download videos and subtitles, access playback and danmaku data, and manage publishing workflows. Publishing actions and high-quality downloads require Bilibili session cookies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle full Bilibili session cookies, which may grant broad account access if exposed.

Mitigation: Use a throwaway Bilibili account for evaluation, avoid sharing primary-account cookies, rotate cookies after use, and provide credentials only for actions that need authentication.

Risk: Credential persistence can leave reusable session cookies on disk.

Mitigation: Keep credentials in memory by default; avoid BILIBILI_PERSIST and credential files unless persistence is required, and remove persisted credentials after use.

Risk: Cookie-bearing HTTP clients and redirects can weaken destination boundaries.

Mitigation: Review outbound network behavior before use, keep requests limited to expected Bilibili domains, and disable cross-origin redirects for authenticated requests during maintenance.

Risk: Publishing actions can modify a Bilibili account or public channel.

Mitigation: Run publishing actions only after checking the dry-run preview and requiring explicit confirmation for account-changing operations.

Risk: Downloads, subtitles, and uploads read or write caller-provided filesystem paths.

Mitigation: Validate output, subtitle, download, and upload paths before execution and run the skill in an isolated working directory when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/bilibili-all-in-one)
- [Project homepage](https://github.com/wscats/bilibili-all-in-one)
- [Publisher profile](https://clawhub.ai/user/zuoyunlai)

## Skill Output:

**Output Type(s):** [text, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, Python examples, structured API results, and generated media or subtitle files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some actions write downloads, subtitles, converted subtitle files, or upload previews to local paths chosen by the caller.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
