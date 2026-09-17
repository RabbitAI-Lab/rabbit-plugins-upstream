## Description:

Provides GIPHY search and retrieval actions for GIFs, stickers, tags, categories, trending content, random content, and phrase translations through the OOMOL GIPHY connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect live GIPHY connector schemas and run validated OOMOL CLI actions for reading GIPHY content through an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes direct execution of remote installer scripts in a shell.

Mitigation: Use connector commands only after the OOMOL CLI is trusted and installed; avoid direct curl | bash or irm | iex installation, prefer a signed or version-pinned installer, review the script first, and verify checksums or publisher signatures when available.

## Reference(s):

- [ClawHub GIPHY Skill](https://clawhub.ai/oomol/skills/oo-giphy)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [GIPHY Homepage](https://giphy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
