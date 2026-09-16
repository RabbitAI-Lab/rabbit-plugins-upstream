## Description:

This skill helps agents retrieve OKSign account, document, linked-document, active-document, and user information through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read OKSign data from a connected account, including credits, document metadata, linked document identifiers, active documents, and configured users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer execution patterns such as curl-to-bash and PowerShell irm-to-iex.

Mitigation: Review and independently verify the OOMOL CLI installer source before running it; prefer signed or checksummed packages, or download and inspect the installer first.

## Reference(s):

- [OKSign homepage](https://www.oksign.be/en/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub OKSign skill page](https://clawhub.ai/oomol/skills/oo-oksign)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-oriented OKSign connector actions after inspecting the live action schema.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
