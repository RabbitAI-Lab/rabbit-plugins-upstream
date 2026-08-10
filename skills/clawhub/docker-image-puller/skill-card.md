## Description:

Downloads Docker images from registries with a Python helper and packages them as tar archives for offline docker load use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaohaixin](https://clawhub.ai/user/zhaohaixin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to pull Docker images through a SOCKS5 proxy or registry mirror and produce tar archives for offline loading. It is useful when images need to be transferred to environments that cannot pull directly from the registry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run background Docker image downloads and write tar archives, which may consume network bandwidth and disk space.

Mitigation: Review the requested image, monitor the background task, and confirm sufficient disk space before large downloads.

Risk: Private registry passwords may be handled unsafely.

Mitigation: Avoid entering sensitive registry passwords unless the skill is updated to use hidden password entry or token-based authentication.

Risk: The configured script path and download mode affect what code runs and which registries or mirrors are contacted.

Mitigation: Verify config.json, the script path, proxy settings, mirror settings, and target architecture before first use or after configuration changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaohaixin/skills/docker-image-puller)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files]

**Output Format:** [Markdown status messages with shell commands and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Docker image tar archives under an images directory and reports docker load commands.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
