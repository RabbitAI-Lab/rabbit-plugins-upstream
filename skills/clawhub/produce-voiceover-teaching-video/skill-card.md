## Description: <br>
Turns supplied narration audio plus an article, notes, screenshots, images, or source videos into a fact-checked faceless vertical teaching video with synchronized captions, cover art, publish copy, hashtags, and a pinned comment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuq87573-create](https://clawhub.ai/user/fuq87573-create) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, editors, and developer-operators use this skill to convert supplied narration and source material into a vertical teaching video with captions, cover art, publishing copy, and delivery QC artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill needs local access to user-provided narration and media files and runs local media tooling. <br>
Mitigation: Use a scoped job directory, provide only the media needed for the job, and authorize only the expected ffmpeg, ffprobe, Python helper, renderer, and browser-rendering actions. <br>
Risk: Network fetching or publishing can expose source material or post content before rights are confirmed. <br>
Mitigation: Do not authorize URL fetching or publishing unless the destination is explicitly scoped and rights for the article, media, voiceover, music, fonts, and logos have been checked. <br>
Risk: Generated teaching videos or publishing copy can contain incorrect or unsupported claims. <br>
Mitigation: Use the skill's frozen-source fact checks, QC report, and delivery validation before release. <br>


## Reference(s): <br>
- [Seven-worker workflow](artifact/references/workflow.md) <br>
- [Artifact contracts](artifact/references/contracts.md) <br>
- [Performance modes](artifact/references/performance.md) <br>
- [Cover and publishing outputs](artifact/references/publishing.md) <br>
- [ClawHub skill page](https://clawhub.ai/fuq87573-create/skills/produce-voiceover-teaching-video) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with shell commands, structured JSON artifact contracts, and generated local media and publishing files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local job artifacts including final.mp4, cover.png, publish-copy.json, captions, manifests, and QC reports.] <br>

## Skill Version(s): <br>
1.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
