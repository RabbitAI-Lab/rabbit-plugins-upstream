## Description:

Use AgentProof for approval-bound repository patches with explicit authority, exactly-once execution, independent verification, deterministic recovery, and signed receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ayobamih](https://clawhub.ai/user/ayobamih)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use AgentProof to route consequential repository patches through explicit approval, execution, receipt verification, and recovery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository patches can mutate consequential files outside the user's intent if transaction boundaries are not checked.

Mitigation: Before execution, verify the repository root, allowed paths, approval source, receipt key, and trusted signer fingerprint.

Risk: Missing or invalid authority, key, fingerprint, repository state, or receipt evidence can make execution or recovery unsafe to continue.

Mitigation: Stop at the relevant protocol boundary and report the missing evidence instead of fabricating approvals, signatures, keys, or receipts.

## Reference(s):

- [AgentProof homepage](https://github.com/AyobamiH/agentproof)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the external agentproof CLI to be installed and available on PATH.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
