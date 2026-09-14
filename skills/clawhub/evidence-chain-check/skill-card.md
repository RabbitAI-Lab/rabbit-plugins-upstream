## Description:

Checks legal or electronic evidence-chain records for monotonic time ordering, subject consistency, and unbroken hash linkage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and agents use this skill to run a lightweight structural check over evidence-chain JSON before human legal or compliance review. It helps identify time-order, subject-consistency, and hash-linkage issues, but does not prove legal admissibility or cryptographic tamper resistance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the structural check as proof of legal evidence integrity or admissibility.

Mitigation: Use the output only as a lightweight screening result and require qualified human legal or compliance review for real evidence decisions.

Risk: Mutable or global installation instructions can install different code than the reviewed artifact.

Mitigation: Install from a pinned, reviewed release or commit and avoid global installation unless operationally required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/evidence-chain-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI output can be plain text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checker returns exit code 0 for complete chains, 1 for detected chain issues, and 2 for usage or parsing errors.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact manifest; artifact SKILL.md frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
