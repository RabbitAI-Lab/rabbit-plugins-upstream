## Description:

Algolia lets agents inspect and manage Algolia indexes, records, rules, and synonyms through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and teams use this skill to work with Algolia data through an OOMOL-connected account, including index discovery, record lookup, browsing, search, and approved record, rule, or synonym changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One-time setup can execute a remote oo CLI installer in the user's shell.

Mitigation: Review the CLI installation path, prefer OOMOL's official source, and verify installer integrity where possible before installation.

Risk: Write and destructive Algolia actions can overwrite or delete records, rules, or synonyms.

Mitigation: Confirm the target index, objectID or filter, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-algolia)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Algolia homepage](https://www.algolia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
