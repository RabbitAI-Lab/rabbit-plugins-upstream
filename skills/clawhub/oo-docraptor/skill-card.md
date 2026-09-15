## Description:

DocRaptor helps agents create hosted PDF or Excel documents from raw HTML or public URLs through an OOMOL-connected DocRaptor account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to create hosted DocRaptor PDF or Excel documents from HTML or public URLs through the OOMOL oo CLI. The skill guides the agent to inspect live action schemas, submit JSON payloads, and return document download URLs and execution metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote shell installer commands.

Mitigation: Install the oo CLI from a verified, versioned source with checksums or signatures instead of piping remote installer scripts directly into a shell.

Risk: The advertised DocRaptor scope is broader than the documented action.

Mitigation: Use the skill only for the documented hosted-document creation workflow unless the publisher clarifies additional supported DocRaptor actions.

Risk: The documented create_hosted_document action creates hosted documents.

Mitigation: Confirm the exact payload and user-visible effect before running the write action.

## Reference(s):

- [ClawHub DocRaptor skill page](https://clawhub.ai/oomol/skills/oo-docraptor)
- [DocRaptor homepage](https://docraptor.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples; connector responses return document URLs and execution metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill tells the agent to inspect live DocRaptor action schemas before constructing payloads and to confirm write-action effects with the user.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
