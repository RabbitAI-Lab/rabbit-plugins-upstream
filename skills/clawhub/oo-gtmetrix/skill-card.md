## Description:

Operates GTmetrix through OOMOL's oo CLI to read GTmetrix account, browser, location, page, report, and test data and to start new performance tests when confirmed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability teams, and external agents use this skill to inspect GTmetrix resources, retrieve reports, monitor test completion, and start performance tests for specified URLs through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installers for the oo CLI.

Mitigation: Use a verified installation method and do not allow an agent to run curl-to-bash or PowerShell installer commands automatically.

Risk: The start_test action changes GTmetrix account state.

Mitigation: Confirm the exact URL and action payload with the user before running the write action.

## Reference(s):

- [GTmetrix homepage](https://gtmetrix.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub GTmetrix skill page](https://clawhub.ai/oomol/skills/oo-gtmetrix)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to shape action payloads and returns connector responses as JSON when actions run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
