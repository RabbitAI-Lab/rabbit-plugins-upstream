## Description:

Build, deploy, and manage Cargo Hosting apps and workers with the Cargo CLI, including Vite single-page apps, serverless edge HTTP handlers, and deployments that promote them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold, deploy, inspect, promote, roll back, and remove Cargo-hosted apps, workers, and deployments from an authenticated Cargo workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Promoting the wrong deployment changes the public live URL for an app or worker.

Mitigation: Verify the deployment UUID, terminal success status, and currently promoted deployment before running a promote command.

Risk: Removing an app or worker also removes its deployments and has no documented undo.

Mitigation: Confirm the app or worker UUID and current live status before removal, and keep the source available so the resource can be recreated if needed.

Risk: Hosted apps and workers consume credits while active.

Mitigation: Remove resources that should no longer be served and review billing or charged-until information before leaving resources live.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [App examples](references/examples/apps.md)
- [Worker examples](references/examples/workers.md)
- [Deployment examples](references/examples/deployments.md)
- [Hosting response shapes](references/response-shapes.md)
- [Hosting troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash command blocks and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the cargo-ai CLI and an authenticated Cargo account before executing hosting commands.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
