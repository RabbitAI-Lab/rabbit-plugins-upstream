## Description:

Feedier helps agents operate Feedier report workflows through an OOMOL-connected account, including reading, creating, updating, deleting, and share-link generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Feedier analytical reports from an agent workflow. It supports listing and retrieving reports, creating or updating report records, deleting reports after explicit approval, and generating expiring report share links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer one-liners for the oo CLI, which can expose users to supply-chain risk if run without verification.

Mitigation: Install the oo CLI only from a trusted, verified source or a pinned release with checksums or signatures, and review the skill before installation.

Risk: Feedier write actions can create, update, or generate share links, and the destructive action can delete reports.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write actions, and require explicit approval before deletion.

## Reference(s):

- [ClawHub Feedier Skill](https://clawhub.ai/oomol/skills/oo-feedier)
- [Feedier Homepage](https://www.feedier.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON data from the Feedier connector; write and destructive operations require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
