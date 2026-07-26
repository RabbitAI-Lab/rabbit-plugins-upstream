## Description: <br>
A lightweight YouTube transcript extraction skill for single-video subtitle retrieval, summaries, content search, question answering, and text export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to retrieve subtitles from a single YouTube video, then summarize, search, answer questions about, or export the transcript text for personal learning and content analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be selected for unrelated SEO or ranking tasks because its trigger wording is broader than its transcript extraction purpose. <br>
Mitigation: Review or narrow the trigger wording before enabling automatic skill selection. <br>
Risk: The packaged workflow references a transcript script that is not present in the artifact. <br>
Mitigation: Supply the missing script or rewrite the workflow to call yt-dlp directly before relying on execution. <br>
Risk: The skill asks the agent to run shell commands and install/use yt-dlp. <br>
Mitigation: Run commands in a reviewed environment and install dependencies only from trusted package sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/youtube-watcher-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with transcript text, summaries, search results, question answers, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-video workflow; generated content depends on available YouTube captions and yt-dlp execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
