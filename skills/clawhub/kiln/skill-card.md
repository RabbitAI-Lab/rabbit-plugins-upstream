## Description:

Kiln lets agents design, slice, queue, monitor, and recover 3D-printing jobs across supported printer backends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[codeofaxel](https://clawhub.ai/user/codeofaxel)

### License/Terms of Use:

AGPL-3.0

## Use Case:

Developers and makers use Kiln to let MCP-capable agents manage 3D printing workflows: find or generate models, slice files, control printers, monitor jobs, and handle fulfillment when configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent access to printers, local network endpoints, camera snapshots, and API keys can expose devices or credentials.

Mitigation: Install only when the publisher is trusted, prefer a pinned reviewed version, use project-scoped MCP configuration, and keep printer/API credentials narrowly scoped.

Risk: Agent-triggered printing, raw G-code, cancellations, and paid fulfillment orders can have physical or financial effects.

Mitigation: Require human confirmation for printing, raw G-code, cancellations, and paid fulfillment orders; review job details before execution.

Risk: Mutable install paths such as latest package installs can change behavior after review.

Mitigation: Pin the reviewed version, prefer versioned package references, and re-review before upgrading.

Risk: 3D printer operation can create hardware, thermal, material, or failed-print hazards.

Mitigation: Use pre-flight checks, G-code validation, temperature limits, printer-specific safety profiles, and human supervision appropriate for the hardware.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/codeofaxel/skills/kiln)
- [Kiln Documentation](https://kiln3d.com/docs)
- [Kiln Agent Guide](https://kiln3d.com/agents?utm_source=github&utm_medium=readme)
- [Kiln Website](https://kiln3d.com)
- [PyPI Package](https://pypi.org/project/kiln3d/)
- [Release Notes v1.4.1](https://github.com/codeofaxel/Kiln/releases/tag/v1.4.1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and structured agent action recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP setup guidance, CLI commands, configuration snippets, model-generation steps, slicing and printing actions, status summaries, and fulfillment workflow guidance.]

## Skill Version(s):

1.4.1 (source: server release, server.json, and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
