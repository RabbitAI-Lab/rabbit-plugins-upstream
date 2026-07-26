## Description: <br>
Generates a three-minute book explainer video from a book title and author, including review script, storyboard, AI illustrations, TTS narration, captions, and final MP4 composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenjun198711](https://clawhub.ai/user/chenjun198711) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and content teams use this skill to turn a book title and author into a short narrated review video workflow. It guides an agent through book research, script and storyboard generation, image and TTS asset creation, subtitle timing, cover generation, and final MP4 assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may send book names, author names, generated narration, image prompts, and caption text to search, image-generation, LLM, and TTS providers. <br>
Mitigation: Use only content appropriate for those providers, review provider terms and retention settings, and avoid sensitive or private material unless the selected services are approved for it. <br>
Risk: Running added scripts or API configuration may perform external calls and local media processing. <br>
Mitigation: Review any scripts and API environment variables before execution, then run the workflow in a controlled workspace with only the credentials required for the selected providers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenjun198711/skills/book-video-generator) <br>
- [Server-resolved GitHub provenance](https://github.com/chenjun198711/book-video-generator) <br>
- [Agent Skills open standard](https://agentskills.io) <br>
- [Volcengine TTS console](https://console.volcengine.com/speech/new) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with JSON snippets, shell commands, and generated media file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce JSON storyboards, image prompts, MP3 narration, ASS subtitles, cover images, and an MP4 output under output/{book_name}_三分钟精读书.mp4.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter says 2.6.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
