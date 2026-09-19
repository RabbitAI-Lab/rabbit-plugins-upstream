## Description:

Hashnode (hashnode.com). Use this skill for Hashnode requests that read, create, update, publish, or delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to let an agent manage Hashnode publications, posts, and drafts through the oo CLI connector while using the user's connected Hashnode account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Install the CLI only through a verified, user-approved method instead of allowing an agent to run the installer one-liners automatically.

Risk: The skill can create, update, publish, and delete Hashnode content through the connected account.

Mitigation: Require user confirmation for write actions and explicit approval for destructive actions, including the exact target and payload.

## Reference(s):

- [Hashnode homepage](https://hashnode.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill page](https://clawhub.ai/oomol/skills/oo-hashnode)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
