## Description: <br>
短视频下载器支持抖音、小红书、快手、视频号、B站、YouTube、Instagram 等主流平台的无水印视频下载，开箱即用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, editors, content collectors, operators, and researchers use this skill to parse supported social-media share links and save watermark-free videos or image-post media locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted media links are sent to redfox.hk for parsing. <br>
Mitigation: Use the skill only when the user is comfortable sharing the submitted link with redfox.hk, and avoid private or tokenized links. <br>
Risk: Downloaded media is saved locally and may include copyrighted or restricted content. <br>
Mitigation: Use the skill only for content the user has rights to download and store, and review the saved files before redistribution or reuse. <br>
Risk: API keys can be exposed if passed in command history or logs. <br>
Mitigation: Prefer REDFOX_API_KEY or a protected config file over command-line API key arguments, and do not hardcode keys in prompts, code, logs, or output files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/video-downloader-redfox) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [README.en.md](artifact/README.en.md) <br>
- [README.md](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, configuration] <br>
**Output Format:** [Terminal text with downloaded media files and optional configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads videos as mp4 files or image posts as sequential image files, normally under ~/Downloads/QoderVideos unless an output directory is provided.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
