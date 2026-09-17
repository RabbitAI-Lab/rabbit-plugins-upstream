## Description:

Woot helps agents search and read Woot offer data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Woot offer details and list live category feeds through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install the oo CLI from an independently verified source with a pinned release, checksum, and signature before using the skill.

Risk: The skill depends on an authenticated OOMOL connection to Woot.

Mitigation: Run Woot actions only after the oo CLI is installed, signed in, and connected; use the skill's read-only actions for offer and feed retrieval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-woot)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Woot Homepage](https://www.woot.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read actions retrieve Woot offer and feed data.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
