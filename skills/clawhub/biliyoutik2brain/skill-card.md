## Description: <br>
BiliYouTik2Brain turns supported video URLs from Bilibili, YouTube, Douyin, and Xiaohongshu into transcripts, structured analysis, knowledge archives, and Markdown or JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[choi8467](https://clawhub.ai/user/choi8467) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to process supported video links into searchable notes, cards, transcripts, OCR-enriched summaries, and local knowledge records. It is intended for video-to-knowledge workflows rather than pure text prompts or non-video links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports automatic use of browser session cookies in some video collection paths. <br>
Mitigation: Avoid logged-in browser sessions for routine processing, disable browser-cookie use where possible, and review cookie-related settings before processing sensitive videos. <br>
Risk: The security review reports that the advertised private mode is not fully enforced by the main CLI and LLM path. <br>
Mitigation: For local-only processing, avoid setting LLM API keys, verify that cloud LLM calls are disabled, and test the intended path before using sensitive content. <br>
Risk: The installer can install packages, use sudo for ffmpeg on supported systems, download models, and create persistent local storage. <br>
Mitigation: Inspect and run preflight checks before installation, prefer an isolated environment, and review created storage locations and permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/choi8467/skills/biliyoutik2brain) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Quality report](artifact/QUALITY-REPORT.md) <br>
- [Meta review](artifact/docs/meta-review-2026-05-15.md) <br>
- [Data quality validation tests](artifact/test/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notes, Obsidian Markdown, rich Markdown with keyframes, JSON data records, and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include transcripts, summaries, knowledge cards, error notes, OCR/keyframe context, comment analysis, and local knowledge-store updates.] <br>

## Skill Version(s): <br>
4.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
