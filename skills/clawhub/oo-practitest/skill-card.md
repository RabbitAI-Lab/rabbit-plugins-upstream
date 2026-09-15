## Description:

PractiTest (practitest.com). Use this skill for ANY PractiTest request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test managers use this skill to operate PractiTest through an OOMOL-connected account, including listing projects and tests, retrieving records, and creating, updating, or deleting tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run an unverified remote installer script for the OOMOL oo CLI.

Mitigation: Prefer an official, inspectable installer or package-manager method with version and integrity verification before installation.

Risk: PractiTest write and destructive actions can modify or permanently delete tests.

Mitigation: Confirm the exact payload, target project or test, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [PractiTest homepage](https://www.practitest.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live PractiTest connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
