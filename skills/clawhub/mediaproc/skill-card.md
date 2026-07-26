## Description: <br>
Process media files (video, audio, images) via a locked-down SSH container with ffmpeg, sox, and imagemagick. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and media-focused agents use this skill to upload files to a trusted mediaproc instance, run whitelisted ffmpeg, sox, and ImageMagick operations, and retrieve processed media outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Files and commands are sent to the configured mediaproc SSH host, so a host controlled by an untrusted operator can observe transferred media and requested operations. <br>
Mitigation: Set MEDIAPROC_HOST only to an instance controlled by the user or a trusted operator, and provision that environment value from controlled configuration. <br>
Risk: The setup flow can involve running a root installer for the mediaproc container host. <br>
Mitigation: Pin the installer to a released tag and review the script before running it with elevated privileges. <br>
Risk: Remote file deletion commands, especially recursive directory deletion, permanently remove data in the mediaproc work directory. <br>
Mitigation: Confirm the exact target path before running delete or recursive delete operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mediaproc) <br>
- [Project homepage](https://github.com/psyb0t/docker-mediaproc) <br>
- [mediaproc releases](https://github.com/psyb0t/docker-mediaproc/releases) <br>
- [lockbox container hardening](https://github.com/psyb0t/docker-lockbox) <br>
- [Setup reference](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the configured mediaproc SSH instance and the media files transferred through it.] <br>

## Skill Version(s): <br>
2.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
