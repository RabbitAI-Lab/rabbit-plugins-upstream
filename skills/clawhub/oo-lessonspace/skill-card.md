## Description:

Operates Lessonspace through OOMOL's oo CLI for reading sessions, creating or retrieving spaces, and retrieving recording URLs without exposing raw API tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Lessonspace from an OOMOL-connected account, including creating or retrieving unified spaces, getting organisation session details, retrieving recording playback URLs, and listing sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running externally downloaded installer commands directly in a shell without verification.

Mitigation: Review setup manually, prefer a signed or checksum-verified release or trusted package manager, and do not let an agent run the curl-to-bash or PowerShell iex commands automatically.

Risk: Lessonspace write actions can change account state, including creating or retrieving unified spaces.

Mitigation: Fetch the live connector schema first and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Lessonspace Skill](https://clawhub.ai/oomol/skills/oo-lessonspace)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Lessonspace Homepage](https://www.thelessonspace.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
