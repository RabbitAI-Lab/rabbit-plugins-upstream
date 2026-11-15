## Description:

Delegates coding work to Codex, Claude Code, Pi, and related coding agents through acpx and the Agent Client Protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to delegate feature work, PR review, refactoring, and codebase exploration to coding agents while managing sessions and fallbacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes broad unattended agent permissions, including auto-approval, bypass-permission modes, and background execution.

Mitigation: Use isolated workspaces with least-privilege credentials, avoid auto-approval or bypass modes unless the risk is explicitly accepted, and monitor long-running sessions.

Risk: The skill relies on third-party agent adapters and command-line tools that may not be pinned in the artifact.

Mitigation: Prefer pinned or preinstalled adapters and review tool versions before using the skill in sensitive repositories.

Risk: Credential-bearing sessions could expose private repositories or API access when used on untrusted code.

Mitigation: Limit available credentials, avoid broad private-repo or API access, and do not run unattended agents on untrusted repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanford/skills/coding-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is oriented around installed coding-agent CLIs and session workflows.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
