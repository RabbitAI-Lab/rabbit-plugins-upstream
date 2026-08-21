## Description:

Create, debug, structure, and run Openplanet AngelScript plugins for Trackmania 2020 (TMNEXT) and ManiaPlanet 4 (TM2/MP4), with guidance on API quirks, AngelScript pitfalls, performance patterns, launch verification, MP4 API mismatch fixes, and reusable templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomekdot](https://clawhub.ai/user/tomekdot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, port, debug, review, and launch Openplanet AngelScript plugins for Trackmania 2020 and ManiaPlanet 4. It is especially useful for checking API compatibility, static preflight issues, launch logs, MP4-specific UI limits, and risky memory-access patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plugin code or guidance may use memory offsets, hooks, native DLL assumptions, or other game-memory operations that can crash the game or behave differently across builds.

Mitigation: Review generated code before running it, verify offsets on the exact target build, prefer read-only telemetry first, and keep write operations behind explicit self-checks and fallback behavior.

Risk: Process-control and destructive maintenance commands can close running games or remove plugin files unexpectedly.

Mitigation: Run these commands only in a controlled development environment, confirm target paths and process names, and keep backups before deleting or moving plugin assets.

Risk: Plugin review or troubleshooting may involve local game, account, map, or log data.

Mitigation: Avoid sending private game, account, map, or log data to third-party APIs without explicit user consent.

## Reference(s):

- [Openplanet API documentation](https://openplanet.dev/docs/api)
- [Openplanet API Reference - Namespaces](references/api-namespaces.md)
- [OpenplanetCore.json - the real source for built-in script namespaces](references/openplanet-core-json.md)
- [MP4 AngelScript verified API facts](references/mp4-api-verified.md)
- [MP4 API Mismatches - Verified Error List & Fixes](references/mp4-api-mismatches.md)
- [MP4 runtime API and Dev memory access](references/mp4-runtime-and-dev-memory.md)
- [Static verification of .as sources](references/static-verify-workflow.md)
- [info.toml Reference and launch verification](references/launch-and-verify.md)
- [Cross-game porting: TMNEXT to MP4](references/crossgame-tmnext-mp4.md)
- [Openplanet UI: Menu Hook & UI Scaling Patterns](references/openplanet-ui-menu-and-scaling.md)
- [Openplanet MP4 UI / UX Rendering Notes](references/mp4-ui-rendering.md)
- [Analyzing a compiled .op plugin and judging portability](references/op-package-analysis-and-porting.md)
- [ClawHub skill page](https://clawhub.ai/tomekdot/skills/openplanet-plugin-dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with AngelScript, TOML, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to inspect local Openplanet reflection JSON, plugin source trees, and launch logs before proposing or modifying plugin code.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
