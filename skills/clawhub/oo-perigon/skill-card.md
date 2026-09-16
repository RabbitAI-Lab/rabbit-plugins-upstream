## Description:

Perigon helps agents search and read Perigon news, entity, topic, story, journalist, source, and Wikipedia data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Perigon news and knowledge data, inspect live connector schemas, and run read-focused Perigon actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes directly running remote installer scripts.

Mitigation: Prefer OOMOL's official install documentation, inspect downloaded installers, and verify integrity where possible before running them.

Risk: Perigon access is mediated through OOMOL as the access layer.

Mitigation: Install only if that access model is acceptable for the intended account and data workflow.

## Reference(s):

- [Perigon homepage](https://perigon.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Perigon skill page](https://clawhub.ai/oomol/skills/oo-perigon)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses use JSON with data and meta.executionId when actions are executed.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
