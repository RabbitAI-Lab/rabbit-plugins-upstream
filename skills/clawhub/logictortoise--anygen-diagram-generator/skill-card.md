## Description:

Generates diagrams, flowcharts, and visual structures such as architecture diagrams, mind maps, org charts, ER diagrams, sequence diagrams, Gantt charts, wireframes, and sitemaps through the AnyGen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[logictortoise](https://clawhub.ai/user/logictortoise)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and other agent users use this skill to turn diagram requests into visual structures, including architecture, process, data, organization, journey, and planning diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram prompts may contain private architecture, network, organization, or workflow details that are sent to an external diagram service.

Mitigation: Use redacted inputs for sensitive diagrams and review whether the external AnyGen service is acceptable for the intended data.

Risk: The skill relies on mutable third-party CLI tooling and may install an additional workflow skill.

Mitigation: Verify the AnyGen CLI package and any workflow skill version before installation, and avoid unattended installs unless the publisher and update channel are trusted.

Risk: Diagram generation requires authentication through an API key or browser login.

Mitigation: Store ANYGEN_API_KEY securely, avoid placing credentials in prompts or logs, and rotate the key if it may have been exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/logictortoise/skills/anygen-diagram-generator)
- [AnyGen website](https://www.anygen.io)
- [AnyGen CLI package](https://www.npmjs.com/package/@anygen/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions with CLI commands and generated diagram artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AnyGen CLI authentication through ANYGEN_API_KEY or browser login.]

## Skill Version(s):

3.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
