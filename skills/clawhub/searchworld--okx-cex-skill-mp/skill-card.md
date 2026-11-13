## Description:

Browse, search, install, update, verify, and remove AI trading skills from the OKX Skills Marketplace.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-assistant operators use this skill to discover, install, update, remove, and verify marketplace skill packages for local agent environments. It provides operational guidance for the OKX CLI and fallback MCP-based search and download flows, but does not place trades or manage accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add, overwrite, or remove third-party skills across multiple local agents.

Mitigation: Review each target skill before installing or updating it, and install only from publishers the user trusts.

Risk: The documented `--force` option bypasses signature verification.

Mitigation: Avoid `--force` unless the package has been independently verified and the user accepts the recorded bypass status.

Risk: Installed marketplace skills can influence future local agent behavior.

Mitigation: Treat installed skills like local software: inspect their SKILL.md files, verify signatures when available, and remove skills that are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-skill-mp)
- [Publisher profile](https://clawhub.ai/user/searchworld)
- [OKX homepage](https://www.okx.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell commands and command output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI or MCP tool steps for marketplace management; does not produce trade orders.]

## Skill Version(s):

1.4.8 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
