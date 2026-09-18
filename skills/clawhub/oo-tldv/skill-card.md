## Description:

Operates tl;dv through an OOMOL-connected account using the oo CLI for meeting retrieval, notes, transcripts, listing, and recording import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate tl;dv from an agent through their OOMOL-connected account. It supports reading meeting records, notes, and transcripts, listing meetings, and importing public recordings after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI only through a trusted, reviewed process with version pinning or verification where possible.

Risk: The import_meeting action changes tl;dv state by importing a publicly accessible recording URL.

Mitigation: Confirm the exact URL, payload, and expected effect with the user before running the write action.

## Reference(s):

- [tl;dv homepage](https://tldv.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tldv)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live action schemas are inspected before payload construction; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
