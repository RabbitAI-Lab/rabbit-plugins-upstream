## Description:

Keeper SCIM helps agents search and read Keeper SCIM users, groups, and service provider configuration through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Keeper SCIM action schemas and perform read-only user, group, and service-provider-configuration queries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary code if run automatically or without verification.

Mitigation: Install the oo CLI only through an approved, verified method and do not allow agents to run remote installer commands automatically.

Risk: Future connector versions could add write or destructive Keeper SCIM actions beyond the read-only actions described in this release.

Mitigation: Use this version only for documented get and list operations, inspect the live action schema before each request, and require explicit user approval for any action marked write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-keeper-scim)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Keeper SCIM homepage](https://www.keepersecurity.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema and run commands; connector responses are JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
