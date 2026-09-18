## Description:

Operates Web of Science through an OOMOL-connected account for document and journal search and retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and developers use this skill to search Web of Science documents and journals, then retrieve document or journal records through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute shell scripts directly.

Mitigation: Do not let an agent run the installer automatically; install the oo CLI only through a trusted, user-approved method with version and integrity checks where possible.

## Reference(s):

- [Web of Science homepage](https://clarivate.com/academia-government/scientific-and-academic-research/research-discovery-and-referencing/web-of-science/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI and a connected Web of Science account.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
