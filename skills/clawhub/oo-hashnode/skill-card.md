## Description:

Provides an OOMOL Hashnode connector workflow for reading profiles, publications, posts, and drafts, and for creating, updating, publishing, or deleting Hashnode content with confirmation for state-changing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to let an agent interact with Hashnode through the OOMOL `oo` CLI, including authenticated profile lookup, publication discovery, post reads, draft reads, and controlled publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions run remote installer scripts directly in a shell.

Mitigation: Review and verify the OOMOL CLI installation method before running installer commands, and do not allow an agent to run remote installer commands automatically.

Risk: Write and destructive Hashnode actions can change or delete publication content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions tagged as write or destructive.

## Reference(s):

- [Hashnode homepage](https://hashnode.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Hashnode post Markdown, rendered HTML, publication data, draft data, user profiles, and connector execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
