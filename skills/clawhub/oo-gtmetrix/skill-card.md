## Description:

Provides agent access to GTmetrix account, page, report, test, browser, location, and simulated-device actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect GTmetrix resources, retrieve performance reports, monitor tests, and start new URL performance tests from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Install the oo CLI only from official, verifiable documentation or a trusted package manager, review downloaded installers before execution, and do not allow an agent to run curl-to-shell or PowerShell Invoke-Expression automatically.

Risk: The start_test action can create a new GTmetrix performance test for a URL.

Mitigation: Confirm the exact URL and action payload with the user before running start_test.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gtmetrix)
- [GTmetrix homepage](https://gtmetrix.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
