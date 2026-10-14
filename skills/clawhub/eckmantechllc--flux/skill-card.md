## Description:

Publish events and query shared world state via Flux state engine. Use when agents need to share observations, coordinate on shared data, or track entity state across systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eckmantechllc](https://clawhub.ai/user/eckmantechllc)

### License/Terms of Use:


## Use Case:

Developers and agents use Flux to publish observations, query shared entity state, coordinate across systems, and track service or device status through a shared event-sourced state engine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can delete single entities or batch-delete shared state.

Mitigation: Require human confirmation before delete and batch-delete commands, and scope tokens to the smallest namespace and permissions available.

Risk: The skill can update runtime admin configuration when FLUX_ADMIN_TOKEN is set.

Mitigation: Leave FLUX_ADMIN_TOKEN unset by default and provide it only for an explicit, reviewed admin action.

Risk: Published events and entity properties may persist in shared state.

Mitigation: Do not publish secrets, personal data, or sensitive operational details unless the endpoint and retention policy are approved for that data.

Risk: Commands send data to the configured Flux endpoint.

Mitigation: Use the default public endpoint or a custom FLUX_URL only when the endpoint and its operators are trusted.

## Reference(s):

- [Flux API Reference](artifact/references/api.md)
- [ClawHub Flux skill page](https://clawhub.ai/eckmantechllc/skills/flux)
- [Flux public API endpoint](https://api.flux-universe.com)
- [Flux project repository](https://github.com/EckmanTechLLC/flux)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires FLUX_TOKEN for the public instance; FLUX_URL and FLUX_ADMIN_TOKEN are optional environment variables.]

## Skill Version(s):

2.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
