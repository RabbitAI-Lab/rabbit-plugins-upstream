## Description:

Pinpoint lets an agent search and read Pinpoint applications, candidates, and jobs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Pinpoint recruiting data, including applications, candidates, and jobs, through the oo CLI with account credentials handled by OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could run unverified code if executed automatically.

Mitigation: Have the user install the oo CLI from a verified source and do not run pipe-to-shell installer commands automatically.

Risk: The skill accesses data from the user's connected Pinpoint account through OOMOL.

Mitigation: Install only if the user trusts OOMOL with connected Pinpoint account data, and keep login or connection setup user-approved.

Risk: Future state-changing Pinpoint actions could modify account data if added or invoked without review.

Mitigation: Require user confirmation of payload and effect before any write action, and explicit approval for destructive actions.

## Reference(s):

- [ClawHub Pinpoint Skill](https://clawhub.ai/oomol/skills/oo-pinpoint)
- [Pinpoint Homepage](https://www.pinpointhq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return Pinpoint account data as JSON through the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
