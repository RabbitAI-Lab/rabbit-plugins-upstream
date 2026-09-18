## Description:

Audit and port AI agent skills, Claude Code skills/plugins, Codex skills/plugins, Gemini CLI skills/extensions, slash commands, agents, hooks, policies, MCP-backed plugins, and similar skill repositories across target agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yand](https://clawhub.ai/user/yand)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Skill Port to inspect agent skill or plugin repositories, assess portability and security, and either produce compatibility reports or stage target-agent layouts for Claude Code, Codex, Gemini CLI, or Agent Skills-compatible runtimes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled auditor can read outside the chosen source through symlinks.

Mitigation: Use the skill only on trusted or sandboxed source directories until symlinks are rejected and file-size limits are enforced.

Risk: Some validation guidance could execute mutable third-party code.

Mitigation: Do not run the npx validation command unless the package source and version are pinned and reviewed.

Risk: Target-agent inference may select an unintended runtime.

Mitigation: Pass --target-agent explicitly when running the bundled auditor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yand/skills/skill-port)
- [Publisher profile](https://clawhub.ai/user/yand)
- [Project homepage](https://github.com/yand/skill-port)
- [Ecosystem Porting](references/ecosystem-porting.md)
- [Location Policy](references/locations.md)
- [Portability Model](references/portability-model.md)
- [Report Schema](references/report-schema.md)
- [Security Review](references/security.md)
- [Claude Source Adapter](references/source-claude.md)
- [Codex Source Adapter](references/source-codex.md)
- [Gemini Source Adapter](references/source-gemini.md)
- [Claude Target Adapter](references/target-claude.md)
- [Codex Target Adapter](references/target-codex.md)
- [Gemini Target Adapter](references/target-gemini.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON reports, staged files, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit-only mode is read-only; port mode may stage target-agent files under explicit output paths.]

## Skill Version(s):

0.1.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
