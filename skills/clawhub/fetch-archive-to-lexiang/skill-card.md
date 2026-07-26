## Description: <br>
Discover and fetch articles, videos, podcasts, and PDFs into standardized source packages, then orchestrate deduplicated Lexiang archival. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajaxhe](https://clawhub.ai/user/ajaxhe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to collect web articles, YouTube videos, podcasts, and PDFs into standard source packages, then archive processed Markdown and media into Lexiang with directory reuse and duplicate checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reuse logged-in browser sessions and access browser cookies while collecting sources. <br>
Mitigation: Run it only for intended sources, use a dedicated browser profile, and avoid unrelated private sessions during collection. <br>
Risk: The skill can read Lexiang-related local credentials and upload archived content or media. <br>
Mitigation: Use least-privilege Lexiang credentials, confirm the target knowledge base or directory, and review upload results before relying on them. <br>
Risk: Logs may partially expose token material during credentialed upload flows. <br>
Mitigation: Review and redact logs before sharing them, and avoid running credentialed operations in public or persistent terminals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ajaxhe/skills/fetch-archive-to-lexiang) <br>
- [README](artifact/README.md) <br>
- [Lexiang Upload Reference](artifact/references/lexiang-upload.md) <br>
- [PDF Processing Reference](artifact/references/pdf-processing.md) <br>
- [YouTube Video Reference](artifact/references/youtube-video.md) <br>
- [Podcast Audio Reference](artifact/references/podcast-audio.md) <br>
- [Platform-Specific Reference](artifact/references/platform-specific.md) <br>
- [Troubleshooting Reference](artifact/references/troubleshooting.md) <br>
- [Lessons Learned](artifact/references/lessons-learned.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown source packages, JSON metadata, downloaded media files, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces standard work packages with source.md, meta.json, optional images or media, and final Markdown for Lexiang upload orchestration.] <br>

## Skill Version(s): <br>
4.1.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
