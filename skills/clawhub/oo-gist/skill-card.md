## Description:

Operate GitHub Gist through OOMOL's oo CLI for reading, creating, updating, deleting, starring, forking, and commenting on gists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with GitHub Gist through an OOMOL-connected account, including reading gists and performing confirmed write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may execute a remote installer for the oo CLI.

Mitigation: Review the official oo CLI install documentation or use a verified install path before approving setup.

Risk: The OOMOL connector can act on a connected GitHub Gist account.

Mitigation: Install and connect the skill only if the publisher is trusted and the account connection is appropriate for the intended use.

Risk: Write and destructive actions can create, update, delete, star, unstar, fork, or comment on gists.

Mitigation: Confirm the exact gist ID, payload, and intended effect before approving any write or destructive action.

## Reference(s):

- [Gist homepage](https://gist.github.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gist)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect the live connector schema before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
