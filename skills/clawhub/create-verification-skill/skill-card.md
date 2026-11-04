## Description:

Generate a project-local verify-<app> skill on top of e2e, so any coding agent can launch the app, check it is worth driving, exercise a feature the way a user does, keep evidence, and bug bash it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to inspect an application repository and generate a project-specific verification skill, feature map, and e2e checks that help prove user-visible behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification workflows can change application data.

Mitigation: Use an isolated development instance and dedicated test accounts.

Risk: The external e2e package and sibling e2e skill are not bundled with this release and were not audited here.

Mitigation: Review the downloaded tooling and generated MCP configuration, and prefer reviewed dependency versions.

Risk: Screenshots and traces may contain private information, and model-based exploration may send data to a provider.

Mitigation: Keep evidence private and check provider data settings before enabling model-based exploration.

## Reference(s):

- [e2e skill homepage](https://e2e.com)

## Skill Output:

**Output Type(s):** [Files, Markdown, Configuration instructions, Code, Shell commands]

**Output Format:** [Project-specific Markdown skill and feature map, with e2e configuration and test files where needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated for the inspected project; includes a verification run and evidence instructions]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
