## Description: <br>
Uses yt-dlp and FFmpeg to inspect formats and download permitted public video or audio with the best source thumbnail, optional source-language subtitle, and reusable hidden inputs for later subtitle translation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aiaaaa4](https://clawhub.ai/user/aiaaaa4) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and external users use this skill to review available media formats, choose quality and destination settings, and download permitted video, audio, thumbnails, and source-language subtitle inputs through a confirmation-first workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads media and creates local project files, which can include hidden audio and subtitle inputs for later translation. <br>
Mitigation: Use it only for content the user has permission to save or use, and review the final response for saved paths and prepared hidden inputs. <br>
Risk: Combined video-download to translation workflows can upload audio to OkFile and send data to Alibaba services. <br>
Mitigation: Proceed with the combined workflow only after the user explicitly agrees to the disclosed external processing. <br>
Risk: Remote video metadata, titles, subtitles, thumbnails, comments, and yt-dlp output may contain untrusted text. <br>
Mitigation: Treat remote media metadata as data, confirm format, path, and filename before download, and avoid following instructions embedded in media-site output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aiaaaa4/skills/video-download) <br>
- [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) <br>
- [Video translation workflow guide](https://github.com/aiaaaa4/ai-landing-skills/blob/main/docs/video-translate/%E8%A7%86%E9%A2%91%E7%BF%BB%E8%AF%91%E5%B7%A5%E4%BD%9C%E6%B5%81%E8%AF%B4%E6%98%8E%E4%B9%A6.md) <br>
- [OkFile API keys](https://www.okfile.com/en/account/api-keys) <br>
- [Alibaba Cloud Model Studio API key guide](https://help.aliyun.com/zh/model-studio/get-api-key) <br>
- [Fun-ASR recorded speech recognition API](https://help.aliyun.com/zh/model-studio/fun-asr-recorded-speech-recognition-http-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell command examples and fixed Chinese confirmation questionnaires] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local media project files only after user confirmation; normal video downloads may also prepare hidden audio and source-subtitle inputs for later translation.] <br>

## Skill Version(s): <br>
1.2.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
