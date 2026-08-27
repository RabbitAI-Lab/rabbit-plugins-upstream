## Description:

Give AI agents and automations their own GitHub App identity so git and gh operations can use GitHub App installation tokens instead of a personal account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eliasempresas](https://clawhub.ai/user/eliasempresas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation maintainers, and AI-agent operators use this skill to configure ghapp so git and GitHub CLI actions authenticate as a GitHub App. It is useful when commits, pull requests, and repository operations need bot attribution or separate GitHub App profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Printed installation tokens or private keys could be exposed if command output, logs, or files are shared broadly.

Mitigation: Treat tokens and private keys as secrets, avoid logging token output, and restrict access to key files and agent transcripts.

Risk: ghapp changes local git and GitHub CLI authentication behavior on the configured machine.

Mitigation: Install only on machines intended to authenticate through the GitHub App, check auth status after setup, and run auth reset when the integration is no longer needed.

Risk: Multiple clients or organizations could be mixed if the same profile is reused across contexts.

Mitigation: Use separate ghapp profiles for separate clients or organizations and set GHAPP_PROFILE deliberately in shells, CI jobs, and agent environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eliasempresas/skills/github-app)
- [ghapp CLI homepage](https://github.com/eliasempresas/ghapp-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the ghapp binary and a GitHub App ID, installation ID, and private key.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
