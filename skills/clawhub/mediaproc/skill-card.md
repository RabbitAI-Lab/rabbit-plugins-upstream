## Description: <br>
Process media files (video, audio, images) via a locked-down SSH container with ffmpeg, sox, and imagemagick. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to upload media to a trusted mediaproc SSH instance, run whitelisted media-processing tools, and download processed files or metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A misconfigured or untrusted MEDIAPROC_HOST can receive files and commands intended for a trusted mediaproc instance. <br>
Mitigation: Provision MEDIAPROC_HOST and MEDIAPROC_PORT as trusted configuration and do not let untrusted callers set them. <br>
Risk: The setup flow can involve reviewing and running an installer with elevated privileges. <br>
Mitigation: Pin the installer to a released tag and review the installer before running it as root. <br>
Risk: Remote delete operations permanently remove files or directories in the mediaproc work directory. <br>
Mitigation: Confirm exact remote paths before running remove-file, remove-dir, or remove-dir-recursive. <br>


## Reference(s): <br>
- [mediaproc setup](references/setup.md) <br>
- [docker-mediaproc](https://github.com/psyb0t/docker-mediaproc) <br>
- [docker-lockbox](https://github.com/psyb0t/docker-lockbox) <br>
- [docker-mediaproc releases](https://github.com/psyb0t/docker-mediaproc/releases) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mediaproc) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations and streamed file input/output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ssh, MEDIAPROC_HOST, MEDIAPROC_PORT, and a trusted running mediaproc instance.] <br>

## Skill Version(s): <br>
2.0.11 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
