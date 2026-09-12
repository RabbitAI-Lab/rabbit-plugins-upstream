## Description:

session-sync reads local session histories from multiple AI coding agents, imports conversations into dsh for continued work, and exports sessions as Markdown archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chendestiny](https://clawhub.ai/user/chendestiny)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to migrate, continue, inspect, or archive local AI coding-agent conversations across supported tools while keeping a human in control of write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool can read private local chat histories from many AI-agent stores.

Mitigation: Install only when broad local session migration is intended, review a pinned versioned source, and limit sources and scopes before applying changes.

Risk: Write, restore, attach, and prune operations can modify multiple local agent stores.

Mitigation: Run self-tests and dry-runs first, keep target applications fully closed during write or restore operations, and verify imported data after applying changes.

Risk: Pipe-to-shell installers and a local Web UI increase operational exposure.

Mitigation: Prefer reviewed package installation over pipe-to-shell commands and stop the Web UI when it is no longer needed.

## Reference(s):

- [Server-resolved source repository](https://github.com/Chendestiny/agent-session-sync)
- [Operator manual](AGENTS.md)
- [English README](README_EN.md)
- [Session format documentation](docs/FORMATS.md)
- [Known operational pitfalls](docs/pitfalls.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run planning, interactive confirmations, session filtering, archive export, and local dashboard views.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
