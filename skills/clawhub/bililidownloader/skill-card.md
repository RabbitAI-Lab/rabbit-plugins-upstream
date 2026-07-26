## Description: <br>
Download Bilibili videos after asking the user for the Bilibili URL, with support for single-video and batch playlist downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[caiyundc880518](https://clawhub.ai/user/caiyundc880518) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to request a Bilibili video URL from the user, inspect available formats, and run a local yt-dlp based download for a single video or playlist. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads Bilibili media to local storage through yt-dlp. <br>
Mitigation: Confirm the URL, selected format, and batch setting with the user before running the command, and expect output files in the current working directory. <br>
Risk: Restricted or account-gated content may require cookies. <br>
Mitigation: Avoid providing account cookies unless they are deliberately needed for the requested content and approved by the user. <br>
Risk: The dependency declaration allows older yt-dlp versions. <br>
Mitigation: Prefer installing or updating to a current yt-dlp release before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/caiyundc880518/skills/bililidownloader) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, text] <br>
**Output Format:** [Markdown guidance with CLI command examples and terminal status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads are saved to the current working directory unless the script is changed or invoked from another directory.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
