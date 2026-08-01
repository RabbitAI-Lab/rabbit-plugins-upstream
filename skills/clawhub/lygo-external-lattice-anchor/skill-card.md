## Description: <br>
Use when the user asks to verify public LYGO lattice mirrors, build a public verify manifest, map eggs to Haven Star Chart proposals, or plan external free-server sync (Pages/HF/Turbo). Layer C world network. Requires LYGO_STACK_ROOT you trust. HTTP GET + local JSON under that stack. Verify is non-mutating by default; snapshot needs --i-consent. No auto git/HF/ClawHub publish. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
LYGO SOVEREIGN LICENSE v2.0 <br>


## Use Case: <br>
Developers and operators working with the LYGO protocol stack use this skill to verify public Layer C mirrors, create local public verification manifests, prepare Star Chart proposal JSON, and plan external synchronization while keeping local A/B data authoritative. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user may point LYGO_STACK_ROOT at an untrusted checkout and then enable builder or refresh actions. <br>
Mitigation: Keep LYGO_STACK_ROOT pointed at a checkout the user controls, and only use --build-manifest or --refresh-local with --i-trust-stack when the user has requested local rebuilds. <br>
Risk: Opt-in flags can write local reports, manifests, proposal files, or consented snapshots. <br>
Mitigation: Run default verification first; use --write-report, --refresh-local, --build-manifest, or --execute-local-only only when the user intentionally wants those local writes. <br>
Risk: Public mirrors can be stale, degraded, or misleading relative to the local LYGO stack. <br>
Mitigation: Treat public HTTPS data as mirror evidence only, verify local A/B layers first, and do not rewrite local eggs from public mirror results. <br>


## Reference(s): <br>
- [Agent Contract](references/AGENT_CONTRACT.md) <br>
- [Security Reference](references/SECURITY.md) <br>
- [ClawHub Skill Listing](https://clawhub.ai/deepseekoracle/skills/lygo-external-lattice-anchor) <br>
- [World Lattice Layer Documentation](https://github.com/DeepSeekOracle/lygo-protocol-stack/blob/main/docs/WORLD_LATTICE_LAYER.md) <br>
- [Haven Star Chart](https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChart.html) <br>
- [Eternal Haven Hub](https://eternalhaven.ca/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with Python commands and optional JSON files or reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default verification is non-mutating; report, manifest, proposal, and snapshot writes require explicit opt-in flags and trusted stack context.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter, claw.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
