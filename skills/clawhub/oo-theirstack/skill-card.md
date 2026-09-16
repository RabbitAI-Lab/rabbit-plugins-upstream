## Description:

TheirStack helps agents search and read TheirStack data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate TheirStack through an OOMOL-connected account for company search, job search, technographic lookup, buying-intent keyword lookup, and team credit balance retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path recommends executing remote installer scripts directly from the shell.

Mitigation: Prefer an official package manager or downloaded, versioned installer that can be verified and inspected; avoid running curl-to-bash or irm-to-iex from an elevated shell unless the user accepts that risk.

Risk: Connector actions depend on authenticated OOMOL and TheirStack account state.

Mitigation: Run first-time setup steps only after commands fail with matching authentication, connection, scope, credential, app, or billing errors.

## Reference(s):

- [TheirStack homepage](https://theirstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL TheirStack connection settings](https://console.oomol.com/app-connections?provider=theirstack)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-theirstack)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
