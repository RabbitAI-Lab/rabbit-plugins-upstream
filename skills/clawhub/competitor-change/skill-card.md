## Description:

Summarizes observable changes in authorized Amazon competitor product snapshots over supported daily or weekly periods using deterministic diffs and existing review counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace users and operators use this skill to create, manage, and read competitor-product watch digests for authorized Amazon ASINs across supported sites and daily or weekly periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI has broader ARI account capabilities than the narrow competitor-watch workflow suggests, including account data access, settings changes, exports, and paid AI actions with the same API key.

Mitigation: Use a scoped API key where available, install only if you trust the ARI provider, avoid autoconfirm, and restrict agent invocation to watch commands unless broader actions are explicitly approved.

Risk: The watch workflow is documented as requiring CLI availability confirmation, so expected watch subcommands may be unavailable in the installed environment.

Mitigation: Run `python scripts/ari.py watch --help` before use and stop with an upgrade prompt if watch commands are unavailable.

## Reference(s):

- [Amazon competitor change monitoring reference](references/reference.md)
- [Watch workflow reference](references/watch-workflow.md)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-change)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and watch digest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and authorized competitor/product access; artifact documentation states deterministic watch digests do not use paid LLM analysis.]

## Skill Version(s):

1.4.7 (source: evidence release metadata, SKILL.md frontmatter, CHANGELOG.md, _meta.json, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
