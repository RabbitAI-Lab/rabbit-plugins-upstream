## Description:

Productboard enables agents to search and read Productboard workspace data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, product operations teams, and agents supporting them use this skill to retrieve Productboard entities, notes, members, teams, and configuration data through an OOMOL-connected Productboard account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-line installer commands fetch and execute remote scripts on the user's machine.

Mitigation: Avoid running installer commands unless the OOMOL installer source is trusted and verified; prefer a pinned, checksum-verified, or package-manager installation path.

Risk: Connector requests may access Productboard workspace data through an authenticated OOMOL-connected account.

Mitigation: Use the skill for read and list Productboard tasks, inspect live action schemas before requests, and confirm payloads before any state-changing action if one is introduced.

## Reference(s):

- [ClawHub Productboard skill page](https://clawhub.ai/oomol/skills/oo-productboard)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Productboard homepage](https://www.productboard.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
