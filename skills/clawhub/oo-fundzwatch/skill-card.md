## Description:

FundzWatch (fundzwatch.ai) helps agents read, create, and update FundzWatch data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected FundzWatch account for market intelligence, watchlists, funding signals, hiring signals, benefits, broker, lender, renewal, usage, and lead data. It supports read actions directly and requires user confirmation before write actions change FundzWatch state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup uses remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer source first, prefer a signed or package-managed oo CLI release, or verify a pinned checksum or signature before running it.

Risk: Running installer commands from an elevated shell can increase impact if the installer source is compromised or unexpected.

Mitigation: Run installation from a normal user shell and grant elevated permissions only when the installer clearly requires and explains them.

Risk: The add_to_watchlist action changes FundzWatch account state.

Mitigation: Confirm the exact JSON payload and expected account change with the user before allowing the write action to run.

## Reference(s):

- [FundzWatch ClawHub Skill](https://clawhub.ai/oomol/skills/oo-fundzwatch)
- [FundzWatch Homepage](https://fundzwatch.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return FundzWatch connector JSON responses through the oo CLI, including data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
