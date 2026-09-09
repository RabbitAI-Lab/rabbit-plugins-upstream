## Description:

Authors a narrated presentation and publishes it to a shareable watch URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bisque.cloud](https://clawhub.ai/user/bisque.cloud)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and content authors use this skill to create narrated slide presentations, synthesize narration locally with bisque-voice, and publish the result to a shareable Bisque watch URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends unpinned remote installer scripts for bisque-voice.

Mitigation: Review the installer source and prefer a verified or package-managed installation path before running install or update commands.

Risk: Publishing can upload deck HTML, assets, narration audio, and context.md content using Bisque credentials.

Mitigation: Use the skill only after confirming the intended Bisque account, selected visibility, and sensitivity of all files being published.

Risk: Bisque account access is required for publishing.

Mitigation: Use the intended profile or environment credentials and protect BISQUE_API_KEY, BISQUE_USER_ID, and ~/.bisque/config.json.

## Reference(s):

- [ClawHub present skill page](https://clawhub.ai/bisque.cloud/skills/present)
- [Bisque Cloud](https://bisque.cloud)
- [bisque-voice macOS and Linux installer](https://download.bisque.today/bisque-voice/install.sh)
- [bisque-voice Windows installer](https://download.bisque.today/bisque-voice/install.ps1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated presentation files such as index.html, optional context.md, optional design.md, assets, local audio, and a published watch URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local narration when available and publishes selected presentation content at the configured Bisque visibility.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
