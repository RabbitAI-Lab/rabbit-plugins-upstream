## Description:

FullEnrich helps agents query FullEnrich through the OOMOL `oo` CLI for credit balance, company lookup, and person lookup requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run FullEnrich enrichment actions from an OOMOL-connected workspace, including credit balance checks and company or person lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may lead an agent to run unverified remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI manually from a trusted, verifiable source after inspecting the installer script and accepting the local user-level code execution risk.

Risk: FullEnrich actions depend on live connector schemas and workspace connection state.

Mitigation: Fetch the action schema before each request and only perform setup or reconnection steps when an auth, scope, credential, or connection error occurs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fullenrich)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [FullEnrich homepage](https://www.fullenrich.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before sending JSON payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
