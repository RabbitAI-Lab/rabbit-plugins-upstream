## Description: <br>
Turns supplied narration audio and local article or media sources into a fact-checked vertical teaching video with synchronized captions, cover art, publish copy, hashtags, and a pinned comment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuq87573-create](https://clawhub.ai/user/fuq87573-create) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and production teams use this skill to convert authorized narration, articles, notes, screenshots, and images into a mobile-safe faceless teaching video package. Developers and operators can use the bundled scripts to initialize local jobs, prepare voiceover timing, validate delivery media, and package the skill for release. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Narration, articles, screenshots, and images can contain sensitive or proprietary user media. <br>
Mitigation: Create jobs in an intentional local job directory, keep source media out of the skill directory, and install only when local access to those inputs is acceptable. <br>
Risk: Public posting can create rights, account, or authorization issues if media, voice, music, fonts, logos, or destinations are not confirmed. <br>
Mitigation: Confirm rights for every media category and separately approve any public upload or account action; the skill is designed not to publish automatically. <br>
Risk: Video output can fail technical delivery requirements or include factual, caption, or layout errors. <br>
Mitigation: Use the QC and validation steps for decode, loudness, resolution, cover, publish-copy, safe-area, and factual checks before delivery. <br>
Risk: Speech-rate changes can reduce intelligibility or distort the narration. <br>
Mitigation: Default to 1.0x, preserve pitch during retiming, enforce the configured speed bounds, and require explicit user approval for aggressive speed increases. <br>


## Reference(s): <br>
- [Seven-worker workflow](references/workflow.md) <br>
- [Artifact contracts](references/contracts.md) <br>
- [Performance modes](references/performance.md) <br>
- [Cover and publishing outputs](references/publishing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON reports, and local media artifact paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a local delivery package that can include final.mp4, cover.png, publish-copy.json, subtitles, stage reports, and QC evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
