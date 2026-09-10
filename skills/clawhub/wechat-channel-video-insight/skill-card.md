## Description:

视频号作品透视 helps an agent inspect a single WeChat Channels post from a share link, resolving title, publishing account, publish time, cover, available media, engagement data, object IDs, short links, and share links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when they have a WeChat Channels video share link and need a concise post dossier with metadata, media, and interaction data. It can also support objectId and short-link conversion or generation of a share link for a known video object.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local file upload behavior can send files to the provider if --file, videoUrl, or audioUrl is given a local path, although the advertised WeChat Channels endpoints do not need uploads.

Mitigation: Do not pass local file paths, --file, videoUrl, or audioUrl unless the user explicitly intends to upload that file to the provider.

Risk: Bundled bytecode and unused endpoint catalog entries increase review scope before installation.

Mitigation: Publisher should remove bundled bytecode, remove unused endpoint catalog entries, and disable file upload behavior before the release is treated as low-risk.

Risk: Paid WeChat lookup calls consume account balance after confirmation.

Mitigation: Review the printed fee estimate with the user and only run paid endpoints with --yes after explicit confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-channel-video-insight)
- [We Media API service](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [text, markdown, json, excel files, shell commands, configuration, guidance]

**Output Format:** [Agent guidance with shell commands; script results can be written as Markdown, JSON, or Excel files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a WM_API_KEY. Paid lookups disclose an estimate and require explicit confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
