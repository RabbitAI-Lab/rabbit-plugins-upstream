## Description:

Prerender helps an agent operate Prerender through an OOMOL-connected account for reading, creating, updating, and deleting Prerender data via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Prerender action schemas, submit sitemaps, queue URLs for caching or recaching, clear Prerender caches, and check cache-clear status through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI, and the security evidence flags those installers as unverified.

Mitigation: Install the oo CLI only from a verified, versioned source with checksum or signature validation before using the skill.

Risk: Prerender actions can change service state, including sitemap submission, URL recaching, and cache clearing.

Mitigation: Confirm the exact payload and user intent before running write actions, and require explicit approval before cache-clearing or other destructive actions.

Risk: The skill depends on OOMOL's CLI and Prerender connector to access a connected account.

Mitigation: Use the skill only when the user accepts OOMOL as an intermediary and has connected the intended Prerender account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-prerender)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Prerender Homepage](https://prerender.io)
- [Prerender Icon](https://static.oomol.com/logo/third-party/prerender.svg)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and live connector schemas; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
