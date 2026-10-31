## Description:

Install Android Lab's local Docker images, then build an Android app, boot a private emulator, install APKs and inspect the UI from the app's own directory. Use when an Android build or emulator is needed without a host SDK or ADB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Android Lab to build, install, and inspect Android apps in a private Dockerized environment when they do not have a host Android SDK or ADB.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The emulator helper mounts the Docker socket, which can give it control over the Docker host.

Mitigation: Run emulator workflows on a dedicated Docker host or disposable VM. Build-only commands do not mount the socket.

## Reference(s):

- [Android Lab commands](references/setup.md)
- [Android Lab project](https://github.com/psyb0t/android-lab)
- [Docker daemon attack surface](https://docs.docker.com/engine/security/#docker-daemon-attack-surface)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.15.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
