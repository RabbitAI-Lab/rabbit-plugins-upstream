## Description: <br>
A media file server that serves multimedia files with FRP support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yu-libin](https://clawhub.ai/user/yu-libin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users use this skill to list local MP4 files and return playback links through a WhatsApp-triggered media workflow. It is intended for users who intentionally want a local media server exposed through an FRP domain. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose a local unauthenticated media service through a public FRP domain. <br>
Mitigation: Run it only when public sharing is intended, restrict the media directory to files that may be public, and prefer a version with authentication and explicit tunnel opt-in. <br>
Risk: The skill downloads and executes a native FRP client. <br>
Mitigation: Review the pinned FRP version and hashes before installation and use environments where executing the downloaded binary is acceptable. <br>
Risk: Traffic depends on a third-party relay and public playback links. <br>
Mitigation: Avoid sensitive media, monitor the generated domain, and prefer deployments with restricted CORS, local-only default mode, and safe path handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yu-libin/skills/mediasync-claw) <br>
- [FRP v0.65.0 release](https://github.com/fatedier/frp/releases/tag/v0.65.0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with media playlist links and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns playlist text containing media filenames and playback URLs.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
