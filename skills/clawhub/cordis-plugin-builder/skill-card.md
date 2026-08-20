## Description:

Guides developers through building Cordis plugins for DeepSeek Harness, covering framework concepts, plugin forms, runtime lifecycle, capability mounting, deployment options, testing, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill as a reference for creating, packaging, testing, and troubleshooting Cordis plugins in DeepSeek Harness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plugin code produced with help from this reference may contain unsafe or incorrect behavior if applied without review.

Mitigation: Review generated plugin code before installing or deploying it.

Risk: Third-party package drift can change plugin behavior or introduce vulnerable dependencies.

Mitigation: Pin third-party package versions before installation and deployment.

Risk: Community plugins and hook commands run with the same privileges as the agent environment.

Mitigation: Treat community plugins and hook commands as same-privilege code and isolate hook storage by session.

Risk: Endpoints created with webServer.register can expose data or operations too broadly.

Mitigation: Add authorization and expose only minimal data for any webServer.register endpoint.

## Reference(s):

- [DSH Platform Overview](references/01-overview/dsh-platform.md)
- [API Contract](references/01-overview/api-contract.md)
- [Mental Models](references/01-overview/mental-models.md)
- [Philosophy](references/01-overview/philosophy.md)
- [Inspect Workflow](references/02-workflow/inspect-workflow.md)
- [Plugin Forms](references/02-workflow/plugin-forms.md)
- [Testing](references/02-workflow/testing.md)
- [Agent Lifecycle](references/03-runtime/agent-lifecycle.md)
- [Events Catalog](references/03-runtime/events-catalog.md)
- [Events](references/03-runtime/events.md)
- [Lifecycle](references/03-runtime/lifecycle.md)
- [Hook Tool Data Flow](references/03-runtime/hook-tool-data-flow.md)
- [Identity Seam](references/03-runtime/identity-seam.md)
- [Runtime Seams](references/03-runtime/seams.md)
- [Client UI](references/04-capability/client-ui.md)
- [Dynamic Plugins](references/04-capability/dynamic-plugins.md)
- [Harness Integration](references/04-capability/harness-integration.md)
- [Tool Pipeline](references/04-capability/tool-pipeline.md)
- [Deployment Overview](references/05-deployment/deployment-overview.md)
- [Packaging](references/05-deployment/packaging.md)
- [Implementation Traps](references/06-experience/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code snippets, shell commands, checklists, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; outputs should be reviewed before applying changes to a plugin or deployment.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
