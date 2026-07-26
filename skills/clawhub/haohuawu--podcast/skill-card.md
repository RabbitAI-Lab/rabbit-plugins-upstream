## Description: <br>
Turns an article, blog post, text, URL, or batch of source material into a generated and published podcast episode, and supports metadata-only maintenance for published episodes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haohuawu](https://clawhub.ai/user/haohuawu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to convert source articles or text into two-host podcast scripts, shownotes, synthesized audio, published episode assets, and an RSS feed. It is also used to update shownotes, covers, and feed metadata for existing episodes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Episode text is sent to Doubao/ByteDance for TTS synthesis. <br>
Mitigation: Use only source material that the user has approved for third-party TTS processing, and avoid private or access-controlled content unless explicit permission and cleanup steps are confirmed. <br>
Risk: The skill publishes generated podcast assets, state files, and RSS metadata to a configured TOS bucket. <br>
Mitigation: Confirm TOS credentials, bucket, region, slug, shownotes, and dry-run output before publishing; use metadata-only update commands when only descriptions or feed metadata change. <br>
Risk: The source-fetching guide includes a Chrome proxy-credential recipe for difficult pages and image downloads. <br>
Mitigation: Avoid the proxy-credential flow unless necessary, treat proxy credentials as sensitive, and remove any temporary files or logs that could expose them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haohuawu/skills/podcast) <br>
- [Script format spec](artifact/references/script-spec.md) <br>
- [Shownotes format spec](artifact/references/notes-spec.md) <br>
- [Source fetching guide](artifact/references/source-fetching-guide.md) <br>
- [Images guide](artifact/references/images-guide.md) <br>
- [Podcast channel config schema](artifact/assets/config.schema.json) <br>
- [Doubao speech console](https://console.volcengine.com/speech) <br>
- [Mic tap source sample](https://freesound.org/people/susychristiansen/sounds/149034/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Audio, Guidance] <br>
**Output Format:** [Markdown scripts and shownotes, JSON configuration, shell commands, RSS XML, MP3 audio files, and published episode assets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, ffmpeg/ffprobe, Doubao TTS credentials, and TOS publishing credentials; supports dry-run estimates, resume caching, validation, and metadata-only updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
