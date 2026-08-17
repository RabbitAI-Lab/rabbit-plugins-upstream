## Description:

GitHub (github.com) enables agents to read, create, update, and delete GitHub data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform GitHub repository, branch, commit, file, release, issue, pull request, label, milestone, and workflow operations through the OOMOL GitHub connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write and destructive GitHub actions through the connected account.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval before destructive actions such as deleting repositories, files, refs, releases, or collaborators.

Risk: First-time setup may require installing or authenticating the oo CLI.

Mitigation: Install only when the user wants Codex to use the OOMOL-connected GitHub account, and review the oo CLI installer before running setup.

## Reference(s):

- [GitHub homepage](https://github.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-github)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's OOMOL-connected GitHub account; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.5 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
