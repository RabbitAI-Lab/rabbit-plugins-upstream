## Description: <br>
Searches multiple online archives to find and recover deleted YouTube videos, metadata, and comments using a video ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jimmyhoang963-max](https://clawhub.ai/user/jimmyhoang963-max) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to check whether a deleted, missing, or private YouTube video has archived video content, metadata, comments, or recovery links available from online archive services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user-provided YouTube video ID is sent to an external archive lookup service. <br>
Mitigation: Avoid using the skill for sensitive private links unless the user accepts that the video ID will be queried remotely. <br>
Risk: Archive results may contain only metadata or comments rather than the full video. <br>
Mitigation: Report clearly whether the video file, metadata, comments, or only service-specific notes were recovered. <br>


## Reference(s): <br>
- [Find YouTube Video API endpoint](https://findyoutubevideo.thetechrobo.ca/api/v5/{videoid}) <br>
- [ClawHub skill page](https://clawhub.ai/jimmyhoang963-max/skills/youtube-video-finder-1-0-0) <br>
- [Publisher profile](https://clawhub.ai/user/jimmyhoang963-max) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown summary with recovered archive links, metadata status, comments status, and service notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May optionally request raw metadata or streamed JSONL when the user explicitly asks for advanced debugging data.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, release evidence, and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
