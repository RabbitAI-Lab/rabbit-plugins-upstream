## Description:

Guides agents through creating, checking, previewing, rendering, and publishing HyperFrames video projects with the CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to build and troubleshoot video compositions, review local previews, and render or publish approved work locally or in the cloud.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Floating npx commands may execute an unreviewed CLI version.

Mitigation: Use a pinned or project-local locked HyperFrames CLI.

Risk: Usage checks may read local coding-tool account or session information.

Mitigation: Avoid usage checks unless the user accepts local account and session reads.

Risk: Cloud rendering, publishing, and feedback can transmit project data or reports.

Mitigation: Require explicit consent before uploading, publishing, or filing public issues; disable telemetry if unwanted.

Risk: Infrastructure deployment and destruction can change cloud resources and incur costs.

Mitigation: Require explicit consent before deploying or destroying infrastructure.

## Reference(s):

- [HyperFrames CLI skill listing](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)
- [Scaffolding and initialization](artifact/references/init-and-scaffold.md)
- [Linting and validation](artifact/references/lint-validate-inspect.md)
- [Preview, rendering, and publishing](artifact/references/preview-render.md)
- [Managed cloud rendering](artifact/references/cloud.md)
- [AWS Lambda rendering](artifact/references/lambda.md)
- [Google Cloud Run rendering](artifact/references/cloudrun.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with CLI commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing commands can create project files and rendered media.]

## Skill Version(s):

1.0.57 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
