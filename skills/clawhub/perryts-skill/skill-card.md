## Description: <br>
Perryts helps agents guide developers using the Perry TypeScript-to-native compiler, including compile and run commands, cross-compilation, configuration, standard library APIs, UI, threading, system APIs, widgets, internationalization, plugins, and auto-update workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhenyangze](https://clawhub.ai/user/zhenyangze) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when building or maintaining Perry projects, especially when they need Perry CLI commands, perry.toml configuration guidance, cross-platform build targets, or API examples for native TypeScript applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Perry guidance can include code, build commands, or configuration that may be incorrect for a user's project or platform. <br>
Mitigation: Review generated code, commands, and perry.toml changes before execution, especially for production builds. <br>
Risk: Auto-update, plugin loading, FFI, and the Geisterhand testing server can increase risk if enabled broadly or left active outside development. <br>
Mitigation: Keep these capabilities opt-in, scoped to the intended environment, and disabled or protected outside development builds. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/zhenyangze/PerryTS-Skill) <br>
- [ClawHub skill page](https://clawhub.ai/zhenyangze/skills/perryts-skill) <br>
- [CLI Reference & Configuration](references/cli-reference.md) <br>
- [Perry Standard Library](references/stdlib.md) <br>
- [Multi-Threading](references/threading.md) <br>
- [Native UI](references/ui.md) <br>
- [Platforms](references/platforms.md) <br>
- [Internationalization](references/i18n.md) <br>
- [System APIs](references/system.md) <br>
- [Widgets](references/widgets.md) <br>
- [Plugins & Auto-Update](references/plugins.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; generated commands and code should be reviewed before execution or production use.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
