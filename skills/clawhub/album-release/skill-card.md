## Description: <br>
Ship a complete AI album in one run: cache user-provided lyrics, render tracks through the Suno direct API, generate cover art, build a 1080p album film with karaoke subtitles, upload to YouTube, deploy to an internet radio server, and announce the release. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickflach](https://clawhub.ai/user/nickflach) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and release operators use this skill to run an end-to-end AI album release pipeline from a JSON album config, including music generation, cover art, video assembly, publishing, radio deployment, and announcement workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The pipeline can publish videos and social announcements automatically. <br>
Mitigation: Run first with RELEASE_SKIP="youtube,deploy,announce" and review generated media, upload metadata, and outbound announcement text before enabling publication phases. <br>
Risk: The deployment phase can use local credentials, copy files over SSH, and restart a remote radio service. <br>
Mitigation: Confirm the JSON config, SSH target, destination paths, credentials, and service restart command before enabling deploy. <br>
Risk: The optional lyrics-generation path can import code from HRM_LYRICS_SRC. <br>
Mitigation: Prefer pre-created lyric cache files, or set HRM_LYRICS_SRC only to a code path that has been reviewed and trusted. <br>


## Reference(s): <br>
- [Album Release Pipeline on ClawHub](https://clawhub.ai/nickflach/skills/album-release) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with bash, JSON, Python, and JavaScript file references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational release steps and scripts that may create media files, upload public videos, deploy audio over SSH, restart a remote service, and post announcements when executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
