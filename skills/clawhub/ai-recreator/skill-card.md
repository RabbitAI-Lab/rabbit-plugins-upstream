## Description: <br>
AI video repurposing and digital human dubbing web tool that turns a Douyin or TikTok link into a rewritten, narrated talking-head video through a five-step download, transcribe, rewrite, TTS, and digital-human pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, teams, and developers use this skill to deploy or operate a local web workflow that repurposes short-form video speech into reviewed rewritten text, synthesized audio, and a digital-human talking-head video. Developers can also integrate the workflow through its REST API for task submission, review, TTS, and output retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The web service handles uploaded or downloaded media, generated outputs, and rewrite text that may contain private or sensitive content. <br>
Mitigation: Install only in a local or access-controlled environment, add authentication and output access controls before any shared deployment, and avoid processing private videos or personal likenesses without permission. <br>
Risk: Browser cookies used for video download are account session credentials if real cookies are placed in cookies.txt. <br>
Mitigation: Use cookies only when necessary, protect cookies.txt as a secret, and do not share or commit real browser cookies. <br>
Risk: Generated media and rewritten text may persist under data/output and data/rewrites after processing. <br>
Mitigation: Review retention needs, manually clean retained output and rewrite files, and add scheduled cleanup for deployments that process sensitive content. <br>
Risk: Generated rewritten scripts and digital-human videos may be misleading, inaccurate, or misuse third-party content or likenesses. <br>
Mitigation: Require human review of rewritten text before generation and confirm rights for source content, reference videos, photos, and voice or likeness use. <br>


## Reference(s): <br>
- [Quick Start Guide](references/quickstart.md) <br>
- [Privacy and Data Handling](references/privacy.md) <br>
- [FAQ](references/faq.md) <br>
- [Anti-Patterns Guide](references/anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text, Files] <br>
**Output Format:** [Markdown guidance with bash commands, REST API examples, configuration values, rewritten text, audio files, and generated video files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include persistent media and rewrite artifacts under data/output and data/rewrites; users should review generated text and clean retained files when no longer needed.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
