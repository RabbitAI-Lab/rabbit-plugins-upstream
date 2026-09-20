## Description:

DumplingAI helps agents read, create, and update data through the OOMOL-connected DumplingAI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DumplingAI through an OOMOL-connected account, including checking balance and usage, browsing catalog capabilities, and running DumplingAI actions with schema-checked JSON input.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute a remote installer script without verification.

Mitigation: Review the OOMOL CLI installation path before installation, avoid automatically running remote install commands, and prefer a verified installer or manual installation source.

Risk: The `run` action can perform write operations against the connected DumplingAI account.

Mitigation: Inspect the live action schema and confirm the exact JSON payload and expected effect with the user before running write actions.

## Reference(s):

- [DumplingAI homepage](https://www.dumplingai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [DumplingAI skill page](https://clawhub.ai/oomol/skills/oo-dumplingai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect DumplingAI action schemas and run connector actions with JSON input.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
