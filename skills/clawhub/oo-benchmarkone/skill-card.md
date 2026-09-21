## Description:

BenchmarkONE helps agents handle BenchmarkONE requests for reading, creating, and updating contact data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with BenchmarkONE contacts from an OOMOL-connected account, including contact creation, lookup, metadata listing, and updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes first-time setup guidance that executes a remote installer script if the oo CLI is missing.

Mitigation: Review the installer step before use and prefer official installation documentation with normal verification.

Risk: BenchmarkONE write actions can create or update contact records.

Mitigation: Confirm the exact payload and expected contact changes with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-benchmarkone)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [BenchmarkONE Homepage](https://www.benchmarkone.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing BenchmarkONE connector payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
