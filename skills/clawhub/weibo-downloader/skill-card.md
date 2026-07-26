## Description: <br>
微博下载器 / Weibo Downloader helps agents download Weibo images and videos from standard, mobile, and fx share links using Python requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[belingud](https://clawhub.ai/user/belingud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to download images and videos from individual or batched Weibo URLs into a local output directory. It is intended for workflows that need a Python-only downloader without browser, ffmpeg, gallery-dl, or yt-dlp dependencies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Weibo and passport.weibo.com, automatically creates visitor cookies, and keeps them locally for up to about a year. <br>
Mitigation: Install only if that network behavior is acceptable, treat storage/weibo_cookies.pkl as sensitive, and delete the file when it is no longer needed. <br>
Risk: Server security evidence flags the release as suspicious because long-lived visitor cookies are stored locally in a risky way. <br>
Mitigation: Prefer a version with safer cookie storage, clear opt-in behavior, and cleanup controls before broad deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/belingud/skills/weibo-downloader) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; executed scripts write JPEG and MP4 files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads are grouped by Weibo author and status ID in the selected local output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
