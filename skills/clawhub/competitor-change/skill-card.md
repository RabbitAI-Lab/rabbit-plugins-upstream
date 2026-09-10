## Description:

Summarizes observable changes in authorized Amazon competitor product snapshots on supported daily or weekly watch schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators and agents use this skill to manage authorized competitor product watches and produce deterministic change digests for supported daily or weekly periods. It is for snapshot change monitoring, not real-time market data, sales, inventory, advertising, order, or true return-rate conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes a broader ARI CLI than the advertised competitor-watch workflow.

Mitigation: For monitor use, restrict agents to the documented watch commands and do not invoke analyze, voc, export, workbench, or operations unless those actions and costs are separately intended.

Risk: Use requires an ARI API key and creates server-side daily or weekly watches.

Mitigation: Install only when the user is comfortable granting an ARI key and creating watches; keep the API key scoped to ARI use and review account impact before creating or changing schedules.

Risk: Paid actions may occur through non-watch ARI commands or account autoconfirm settings.

Mitigation: Disable or avoid autoconfirm for paid actions and require explicit user confirmation before any paid analysis, export, workbench, or operations command.

Risk: The watch workflow is documented as planned if the current CLI does not expose watch commands.

Mitigation: Run `python scripts/ari.py watch --help` before use and stop with an upgrade prompt if the watch subcommands are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-change)
- [Amazon 竞品变化监控 专用监控工作流](references/watch-workflow.md)
- [Amazon 竞品变化监控 专用监控参考](references/reference.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured CLI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. The documented watch digest path is deterministic and reports zero analysis credits, while broader packaged ARI commands can perform paid analysis, export, and account or workbench actions.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, CHANGELOG.md, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
