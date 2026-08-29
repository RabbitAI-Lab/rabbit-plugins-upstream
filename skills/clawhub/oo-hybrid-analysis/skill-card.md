## Description:

Hybrid Analysis (hybrid-analysis.com). Use this skill for ANY Hybrid Analysis request - searching and reading data. Whenever a task involves Hybrid Analysis, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to search and read Hybrid Analysis data through an OOMOL-connected account, including API key status, SHA256 file overviews, sandbox report states, report summaries, and detonation reports associated with file hashes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hybrid Analysis requests are routed through OOMOL as an intermediary for the connected account.

Mitigation: Confirm comfort with OOMOL-mediated requests before installation and use only the disclosed Hybrid Analysis connector actions.

Risk: First-time setup may require installing or authenticating the oo CLI and connecting a Hybrid Analysis API key.

Mitigation: Run setup only when a command fails for the matching auth, connection, scope, or CLI-not-found condition.

Risk: Incorrect payloads could send unintended hashes or request parameters to the connector.

Mitigation: Fetch the live connector schema before constructing each payload and keep requests limited to the required action inputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hybrid-analysis)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Hybrid Analysis](https://www.hybrid-analysis.com/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Analysis, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
