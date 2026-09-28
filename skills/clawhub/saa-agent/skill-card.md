## Description:

Enables AI agents to generate images through the Character Select Stand Alone App (SAA) image-generation backend using a command-line client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mirabarukaso](https://clawhub.ai/user/mirabarukaso)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users generate images with an accessible SAA backend, including ComfyUI or WebUI workflows, by supplying prompts and image settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting to an untrusted SAA backend can expose prompts and other data.

Mitigation: Use only a trusted backend and prefer a local trusted endpoint.

Risk: WSS connections may not verify the server's TLS certificate, exposing credentials to interception.

Mitigation: Avoid real credentials over WSS until certificate verification is fixed; review any command that includes usernames or passwords.

Risk: Force-unlocking a backend can disrupt another generation, and a chosen output path can overwrite an existing file.

Mitigation: Require explicit user confirmation before using the skeleton key or overwriting an important output file.

## Reference(s):

- [SAA Agent ClawHub release](https://clawhub.ai/mirabarukaso/skills/saa-agent)
- [SAA setup documentation](https://github.com/mirabarukaso/character_select_stand_alone_app)

## Skill Output:

**Output Type(s):** [Image files, Text]

**Output Format:** [PNG image saved to a local path; optional base64-encoded image on stdout with generation status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running SAA 2.9.0+ backend with SAAC enabled; accepts prompts and generation settings.]

## Skill Version(s):

1.2.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
