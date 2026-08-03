## Description: <br>
Process media files (video, audio, images) via a locked-down SSH container with ffmpeg, sox, and imagemagick. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media-processing agents use mediaproc to upload files to a trusted media-processing container, run whitelisted ffmpeg, sox, and ImageMagick operations, and retrieve generated media outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Files and commands are sent to whichever mediaproc host is configured. <br>
Mitigation: Install only when MEDIAPROC_HOST and MEDIAPROC_PORT point to a host the user controls or trusts. <br>
Risk: Optional server installation can require root privileges. <br>
Mitigation: Review and pin the installer before running it with elevated privileges. <br>
Risk: Remote delete operations can permanently remove files in the mediaproc work directory. <br>
Mitigation: Get explicit confirmation for the exact target path before using remove-file, remove-dir, or remove-dir-recursive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mediaproc) <br>
- [Project homepage](https://github.com/psyb0t/docker-mediaproc) <br>
- [Setup guide](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and media-processing command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or retrieve transformed media files through the configured mediaproc host.] <br>

## Skill Version(s): <br>
2.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
