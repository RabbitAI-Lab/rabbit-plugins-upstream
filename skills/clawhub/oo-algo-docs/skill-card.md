## Description:

AlgoDocs helps agents read, create, and update AlgoDocs data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list AlgoDocs extractors, folders, and extracted records, fetch data for a document, check connected account identity, and import public document URLs into AlgoDocs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run remote installer scripts that execute code on the user's machine.

Mitigation: Review or verify the installer before use, and prefer an official package manager or pinned release when available.

Risk: The upload document action changes AlgoDocs state by importing a public document URL into an extractor and folder.

Mitigation: Confirm the exact URL, extractor, folder, and expected effect with the user before running the write action.

## Reference(s):

- [AlgoDocs homepage](https://algodocs.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AlgoDocs skill on ClawHub](https://clawhub.ai/oomol/skills/oo-algo-docs)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands for AlgoDocs connector actions and guidance for confirming write payloads before execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
