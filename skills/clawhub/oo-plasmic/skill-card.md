## Description: <br>
Plasmic (plasmic.app). Use this skill for searching and reading Plasmic CMS data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to inspect the live Plasmic connector schema, list Plasmic CMS rows, and count matching CMS rows with filters, draft mode, and locale selection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL's oo CLI and a connected Plasmic account, so commands can fail when the CLI is missing, authentication is stale, connection scope is missing, or billing is blocked. <br>
Mitigation: Install only when OOMOL oo CLI and Plasmic access are intended; use the setup fallback only after an auth, connection, or billing failure. <br>
Risk: Broad Plasmic requests could be mistaken for permission to edit or administer Plasmic content beyond the listed read actions. <br>
Mitigation: Treat the skill as appropriate for listing and counting CMS items; require explicit user confirmation and verify the live action schema before any edit, delete, or broader administration action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-plasmic) <br>
- [Plasmic Homepage](https://www.plasmic.app) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before constructing payloads; read actions can be run directly, while write or destructive actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
