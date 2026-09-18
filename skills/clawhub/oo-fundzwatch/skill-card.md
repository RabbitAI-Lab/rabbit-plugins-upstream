## Description:

FundzWatch enables agents to read, create, and update FundzWatch data through OOMOL's oo CLI connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate FundzWatch through a connected OOMOL account, including market intelligence searches, watchlist tracking, funding and hiring signals, benefits and broker data, lender data, usage checks, and controlled write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell and PowerShell installer commands that could execute unverified installer code.

Mitigation: Review the installer source, prefer a verified or checksum-validated oo CLI installation method, and avoid running installer commands in an elevated session unless that access is intentional.

Risk: FundzWatch actions tagged as write can change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval before any destructive action.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-fundzwatch)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [FundzWatch Homepage](https://fundzwatch.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when commands run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
