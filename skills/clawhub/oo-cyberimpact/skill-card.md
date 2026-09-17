## Description:

Cyberimpact helps agents read, create, update, replace, and delete Cyberimpact groups, members, and email templates through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cyberimpact contact groups, members, and email templates from an agent workflow while relying on OOMOL-connected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the required CLI.

Mitigation: Review the CLI installation path carefully and prefer an official package manager or version-pinned installer with checksum or signature verification.

Risk: The skill can perform write and delete actions against Cyberimpact resources.

Mitigation: Confirm the exact target and payload before state-changing actions, and require explicit approval before destructive actions.

## Reference(s):

- [Cyberimpact homepage](https://www.cyberimpact.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cyberimpact skill page](https://clawhub.ai/oomol/skills/oo-cyberimpact)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live Cyberimpact action schema before constructing command payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
