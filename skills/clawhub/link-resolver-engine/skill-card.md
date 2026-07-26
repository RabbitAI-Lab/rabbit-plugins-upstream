## Description: <br>
link-resolver-engine helps an agent identify Bilibili and Douyin video links, resolve high-quality direct media URLs, and save downloaded MP4 files locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to process Bilibili or Douyin links in an OpenClaw agent, download the requested videos, and optionally choose a filename prefix, output directory, or Bilibili format string. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install Python packages, Chromium, and FFmpeg during use. <br>
Mitigation: Run it in an isolated environment and review first-run downloads before using it on a primary workstation. <br>
Risk: The skill downloads media and writes files to default or user-selected directories. <br>
Mitigation: Use a non-sensitive output directory, review requested paths, and avoid giving it privileged or private locations. <br>
Risk: The skill runs subprocesses while resolving and merging media. <br>
Mitigation: Review the scripts and keep execution restricted to the intended Bilibili or Douyin download workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wangminrui2022/skills/link-resolver-engine) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>
- [FFmpeg downloads](https://ffmpeg.org/download.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local MP4 file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python; accepts a video URL, optional filename prefix, optional download directory, and optional Bilibili format string.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
