## Description:

Downloads Douyin videos, image posts, and audio tracks through a selected browser, without third-party downloader accounts or API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and other users use this skill to save Douyin videos, image posts, or audio tracks they are authorized to download as local files. It stops when login, verification, or access restrictions prevent the selected browser from confirming the work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a browser session and a separately installed local Bridge runtime.

Mitigation: Select only the intended browser environment, use a runtime you trust, and prefer reviewed, pinned installation versions.

Risk: Login walls, verification challenges, or restricted detail responses can block access to a work.

Mitigation: Stop at the barrier and handle it in the selected browser; do not retry through, switch environments, or bypass it.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/xxjrq/skills/douyin-download-webbridge)
- [Publisher profile](https://clawhub.ai/user/xxjrq)
- [Easy WebBridge project documentation](https://github.com/xxjrq/easy-webbridge)
- [EasyBR official download page](https://www.ebrower.com/down.html)

## Skill Output:

**Output Type(s):** [Files, Guidance, Shell commands]

**Output Format:** [Local MP4, JPEG, PNG, WebP, or MP3 files with text status and saved paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes one Douyin work per run; saves to the default downloads folder or a user-selected directory. Audio-only output is normalized to 48 kHz stereo MP3.]

## Skill Version(s):

1.1.5 (source: package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
