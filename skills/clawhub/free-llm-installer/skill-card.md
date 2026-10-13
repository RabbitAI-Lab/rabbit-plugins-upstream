## Description:

Installs and checks free language models for WorkBuddy and Claude Code, with optional model switching, monitoring, and image-reading support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy or Claude Code users install free model configurations and test their availability, tool calling, and image support. They can also monitor model status or switch between configured models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Claude Code or WorkBuddy prompts and images may be sent to third-party LLM providers.

Mitigation: Use only approved providers; do not send secrets, private code, customer data, or sensitive images through free gateways.

Risk: Model switching may persistently reroute traffic by changing local settings and profiles.

Mitigation: Review configuration changes and keep backups of settings and profile files.

Risk: Failed-request dumps may retain sensitive transcripts locally, and paid providers may incur charges.

Mitigation: Disable failed-request dumps for sensitive conversations and enable paid providers only with explicit cost controls.

## Reference(s):

- [Free LLM Installer on ClawHub](https://clawhub.ai/oracis/skills/free-llm-installer)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance and local configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write model and profile settings and report live availability checks.]

## Skill Version(s):

1.1.7 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
