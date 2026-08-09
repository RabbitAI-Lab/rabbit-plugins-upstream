## Description:

Review LyraShield release-assurance evidence through OAuth-first, workspace-bound MCP tools with read-only defaults and approval-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ecryptoguru](https://clawhub.ai/user/ecryptoguru)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, release reviewers, and operators use this skill to inspect LyraShield release-assurance evidence, summarize current issues, and explain pending approvals without treating the result as a security guarantee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may grant broader OAuth access than needed for release evidence review.

Mitigation: Confirm the LyraShield MCP connection is trusted and grant only the OAuth scopes needed for the task; keep write access limited.

Risk: Outputs could be mistaken for a complete security verification or guarantee.

Mitigation: Present findings as release-assurance review summaries and do not claim that all Vibe Security 50 controls were verified.

Risk: Dashboard report contents could be copied into prompts unnecessarily.

Mitigation: Link to LyraShield dashboard evidence instead of recreating dashboard UI or copying report contents into prompts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ecryptoguru/skills/lyrashield)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-only defaults; write actions require the lyrashield.write OAuth scope and explicit approval.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
