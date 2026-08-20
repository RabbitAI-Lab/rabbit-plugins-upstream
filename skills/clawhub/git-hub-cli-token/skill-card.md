## Description:

A read-only GitHub CLI skill for AI agents that minimizes token use with compact JSON output, limits, caching, timeouts, retries, and explicit write-operation safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[moniq888](https://clawhub.ai/user/moniq888)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to inspect GitHub repositories, pull requests, issues, CI runs, and source files through read-only GitHub CLI commands while conserving context tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a GitHub CLI login or GITHUB_TOKEN for token-backed read access, including private repository data available to that account.

Mitigation: Install only with a least-privilege token or account, avoid broad private-repository access, and review authentication scope before use.

Risk: Cached command outputs in temporary files may contain private repository data.

Mitigation: Treat temporary cache files as sensitive data and clear them according to the operating environment's data-handling policy.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/moniq888/skills/git-hub-cli-token)
- [Publisher profile](https://clawhub.ai/user/moniq888)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, and Windows CMD command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces compact read-only GitHub CLI workflows using --json, --limit, jq -c, caching, timeout, retry, and truncation guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
