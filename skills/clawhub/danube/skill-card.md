## Description:

Enables agents to discover and use organizational and third-party tools through Danube, with user confirmation before sensitive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can search available Danube tools, inspect their inputs, and use them to work with organizational and connected services after obtaining consent for sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to connected tools can make changes, send data, or spend funds through third-party services.

Mitigation: Use a scoped Danube API key and confirm the exact tool and inputs before write, spend, credential-store, workflow, skill, wallet, or batch actions.

Risk: Retrieved context and examples may contain real organization or account data, and successful calls may save non-secret service defaults.

Mitigation: Share only the data required for a task and review retrieved context and saved defaults before reuse.

## Reference(s):

- [Danube OpenClaw guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube REST API recipes](references/rest-api.md)
- [Danube troubleshooting](references/troubleshooting.md)
- [Danube internal tools guide](https://docs.danubeai.com/organizations/internal-tools)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may contain organization or account data; review actions before execution.]

## Skill Version(s):

8.1.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
