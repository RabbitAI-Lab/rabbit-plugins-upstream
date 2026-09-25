## Description:

Control Chromecast devices on your local network: discover devices, cast media, control playback, manage queues, and save or restore states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[morozred](https://clawhub.ai/user/morozred)

### License/Terms of Use:


## Use Case:

External users and developers use this skill as a command reference for controlling Google Cast devices on a local network with catt, including discovery, casting, playback, queues, and state restore.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control Chromecast or Google Cast-enabled devices on the user's local network.

Mitigation: Run commands only on trusted networks and verify the target device before issuing playback, volume, queue, or state commands.

Risk: Casting local files can expose media to nearby devices or users on the network.

Mitigation: Avoid casting sensitive local files on untrusted or shared networks.

Risk: The skill depends on the external catt command-line package.

Mitigation: Install catt from a trusted package source, and pin or review the package source when stricter supply-chain assurance is required.

## Reference(s):

- [catt GitHub project](https://github.com/skorokithakis/catt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires catt and access to Chromecast or Google Cast-enabled devices on the same local network.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
