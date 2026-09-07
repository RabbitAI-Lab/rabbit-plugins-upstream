## Description:

Tracks saved Amazon listing snapshots and reports deterministic diffs for listing fields such as title, bullet points, and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to create, manage, and read watch digests for saved Amazon product listing snapshots. It is intended for deterministic listing change alerts, not real-time monitoring, listing edits, sales inference, inventory reporting, order data, ad data, or true return-rate analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI includes broader ARI account actions beyond the watch-only listing alert flow, including paid AI analysis, exports, account changes, and auto-confirm behavior.

Mitigation: Use an ARI API key whose permissions and credit exposure are acceptable for the whole CLI, restrict agent use to the documented watch commands, and require explicit user intent before invoking non-watch commands.

Risk: A custom ARI_BASE_URL could redirect API-key-bearing requests away from the intended service.

Mitigation: Avoid setting ARI_BASE_URL unless you control the destination and have intentionally enabled the custom-base workflow.

Risk: The skill may not be usable if the installed CLI does not provide the watch subcommands.

Mitigation: Run `python scripts/ari.py watch --help` before use and stop with an upgrade prompt if the watch commands are unavailable.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/listing-change)
- [Amazon Listing 变化提醒 专用监控参考](references/reference.md)
- [Amazon Listing 变化提醒 专用监控工作流](references/watch-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and the watch CLI commands to be available before use.]

## Skill Version(s):

1.4.7 (source: server evidence, frontmatter, _meta.json, skill-defaults.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
