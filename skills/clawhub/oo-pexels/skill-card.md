## Description:

Pexels (pexels.com) skill for searching and reading Pexels photo, video, collection, and account collection data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, list, and retrieve Pexels photos, videos, collections, and metadata through an authenticated OOMOL-connected Pexels account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance may lead an agent to run an unverified remote installer script if the oo CLI is missing.

Mitigation: Prefer a verified package, a pinned download with checksum or signature verification, or manually inspect the installer before execution.

## Reference(s):

- [Pexels homepage](https://www.pexels.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Pexels skill listing](https://clawhub.ai/oomol/skills/oo-pexels)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
