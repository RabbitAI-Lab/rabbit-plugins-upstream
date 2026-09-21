## Description:

Forem lets agents operate a Forem account through OOMOL to read articles, comments, tags, and the current user, and to create or update authenticated-user articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Forem content through an OOMOL-connected account, including article lookup, listing, comment review, and confirmed article creation or updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the OOMOL CLI installation path before installing; prefer official documentation, signed releases, package-manager installation, or checksum verification.

Risk: Write actions can create or update Forem articles in the connected account.

Mitigation: Check the exact payload and target account before allowing create_article or update_article to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-forem)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Forem homepage](https://www.forem.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI connector commands and confirmation guidance for write actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
