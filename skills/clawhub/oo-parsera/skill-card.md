## Description:

Parsera (parsera.org) helps agents search, read, and extract structured or Markdown data from webpages through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to operate Parsera from an agent session for webpage extraction, Markdown conversion, schema inspection, and parsing of provided HTML or text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that can execute code on the user's machine.

Mitigation: Prefer an official package or a downloaded installer that can be reviewed before execution, and require explicit approval for first-time setup steps.

Risk: Parsera access depends on the OOMOL oo CLI and a connected Parsera account.

Mitigation: Run connector actions only after the user has installed the CLI, signed in, and connected Parsera, and fall back to setup only after an authentication or connection failure.

## Reference(s):

- [Parsera homepage](https://parsera.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-parsera)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.4 (source: release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
