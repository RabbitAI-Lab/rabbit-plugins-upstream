## Description:

Abstract (abstractapi.com). Use this skill for ANY Abstract request - searching and reading data. Whenever a task involves Abstract, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the live Abstract connector schema and run the documented email validation action through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup uses remote installer commands that execute immediately.

Mitigation: Install the oo CLI only through a reviewed, version-pinned, checksum- or signature-verified method, and do not let an agent run curl|bash or irm|iex setup commands automatically.

Risk: The connector depends on an OOMOL-connected Abstract API key and billing state.

Mitigation: Connect credentials through the OOMOL console yourself, keep the agent scoped to the documented email validation action, and resolve billing or connection errors manually.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Abstract homepage](https://www.abstractapi.com/)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-abstract)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
