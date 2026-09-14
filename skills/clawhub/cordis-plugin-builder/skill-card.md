## Description:

Guides developers through building, testing, packaging, publishing, installing, and troubleshooting Cordis plugins for DeepSeek Harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create Cordis plugins for DeepSeek Harness, including environment setup, API-contract inspection, lifecycle-safe implementation, capability mounting, tests, packaging, and installation via dsh plugin add.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production-style templates can expose host or session data when copied into plugins without adequate access control.

Mitigation: Review generated plugins before production use, authenticate HTTP routes, apply per-session authorization, and limit access to host and session data.

Risk: Plugin installation and local skill registration can change a DSH profile or expose model-visible instructions.

Mitigation: Use isolated test profiles, review local skill directories before registration, and require explicit approval before applying profile or bundle changes.

Risk: Unpinned package versions can introduce supply-chain drift during plugin packaging or installation.

Mitigation: Pin package versions, verify release artifacts in an isolated environment, and use least-privilege credentials for publishing or deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiwifruit13/skills/cordis-plugin-builder)
- [Cordis plugin builder guide](SKILL.md)
- [DeepSeek Harness platform overview](references/00-understanding/dsh-platform.md)
- [Cordis core concepts and DSH customization](references/00-understanding/philosophy.md)
- [Plugin forms and complete templates](references/00-understanding/plugin-forms.md)
- [Environment setup](references/10-setup/environment.md)
- [API inspection workflow](references/10-setup/inspect-workflow.md)
- [Scaffolding and initialization](references/10-setup/scaffolding.md)
- [Fiber, effects, and lifecycle](references/20-develop/lifecycle.md)
- [Event dispatch and waterfall semantics](references/20-develop/events.md)
- [Capability mounting in DSH](references/30-capability/harness-integration.md)
- [Tool execution pipeline](references/30-capability/tool-pipeline.md)
- [Cordis plugin testing methodology](references/40-test/testing.md)
- [Deployment overview](references/50-ship/deployment-overview.md)
- [Packaging, cordis.yml, deployment, and diagnostics](references/50-ship/packaging.md)
- [Implementation traps and mitigations](references/90-experience/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with TypeScript, YAML, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged checklists and troubleshooting steps.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
