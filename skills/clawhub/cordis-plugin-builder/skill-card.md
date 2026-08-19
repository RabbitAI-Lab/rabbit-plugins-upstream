## Description:

Guides developers through building, testing, packaging, and deploying Cordis-compatible plugins for DeepSeek Harness, including framework concepts, capability integration, dynamic plugins, Client UI, and deployment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when creating, modifying, testing, or deploying Cordis plugins for DeepSeek Harness. It supports plugin development guidance for services, events, tools, prompts, skills, Client UI surfaces, dynamic plugins, multi-language bridges, packaging, and troubleshooting PENDING or FAILED plugin loads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or installed Cordis/DSH plugins run as local code and may be installed persistently in a profile.

Mitigation: Review plugin code and configuration before running it, use trusted or disposable workspaces where practical, avoid hardcoded secrets, and confirm whether the plugin is temporary or persistent.

Risk: Incorrect plugin wiring can leave dependencies pending, fail plugin loads, or expose unintended tools, prompts, skills, or Client UI surfaces.

Mitigation: Use the bundled inspect workflow and testing guidance to confirm service, event, slot, configuration, and deployment contracts before installing or enabling a plugin.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiwifruit13/skills/cordis-plugin-builder)
- [DeepSeek Harness platform overview](artifact/references/dsh-platform.md)
- [Cordis core concepts and DSH customization](artifact/references/philosophy.md)
- [Cordis inspect workflow](artifact/references/inspect-workflow.md)
- [Plugin forms and complete templates](artifact/references/plugin-forms.md)
- [Capability integration for tools, prompts, skills, and Client UI](artifact/references/harness-integration.md)
- [Cordis lifecycle and effect management](artifact/references/lifecycle.md)
- [Cordis event dispatch patterns](artifact/references/events.md)
- [DSH event catalog](artifact/references/events-catalog.md)
- [Client UI slot and host integration](artifact/references/client-ui.md)
- [Deployment overview](artifact/references/deployment-overview.md)
- [Packaging, cordis.yml, and diagnostics](artifact/references/packaging.md)
- [Cordis plugin testing methodology](artifact/references/testing.md)
- [Common pitfalls and mitigations](artifact/references/traps.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with TypeScript, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include plugin checklists, configuration snippets, and deployment commands; generated or installed plugin code should be reviewed before execution.]

## Skill Version(s):

1.0.0 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
