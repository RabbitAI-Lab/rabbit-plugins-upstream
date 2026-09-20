## Description:

Enables agents to operate GitHub through an OOMOL-connected account for reading, creating, updating, deleting, and searching GitHub data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect GitHub connector schemas and run GitHub actions through the oo CLI for repository, issue, pull request, release, workflow, search, and user operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive GitHub actions through an OOMOL-connected account.

Mitigation: Confirm the target, payload, and expected effect before running any action marked write or destructive.

Risk: Connector access depends on the GitHub scopes granted in OOMOL.

Mitigation: Review the connected GitHub scopes in OOMOL and keep them limited to the intended repositories and operations.

Risk: The fallback setup path includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer OOMOL's official install path or verify the installer source before using pipe-to-shell installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-github)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [GitHub homepage](https://github.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, API calls, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command responses return a JSON object with data and meta.executionId.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
