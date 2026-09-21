## Description:

Exa lets agents read, create, and update Exa data through the OOMOL-connected Exa connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search the web with Exa, retrieve page contents, find similar pages, and generate citation-backed answers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute shell content directly.

Mitigation: Review the installer source and prefer a verified package manager or checksum/signature-validated installer before installing the oo CLI.

Risk: Exa actions are routed through OOMOL's connector service using a connected account.

Mitigation: Connect an Exa account only when that routing model is acceptable for the intended workspace and data.

Risk: Some actions are labeled write or destructive and may change account state.

Mitigation: Confirm the exact action payload and intended effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-exa)
- [Exa homepage](https://exa.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connector can return Exa search results, retrieved page contents, similar-page results, or citation-backed answers.]

## Skill Version(s):

1.0.4 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
