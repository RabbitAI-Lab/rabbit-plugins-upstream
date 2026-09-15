## Description:

Generates LGD-III gated permission policies that divide agent tools into allow, review, and deny lists with trigger, review, release, and retrospective gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to turn an agent tool manifest into a local permission policy that identifies tools an agent may use, tools requiring human review, and tools that should be denied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed or unknown high-risk tool metadata can be classified too permissively.

Mitigation: Reject malformed risk values before policy generation and manually review generated allow, review, and deny lists before using them as a security control.

Risk: Duplicate or ambiguous tool entries can obscure the intended permission boundary.

Mitigation: Deduplicate and normalize tool names in the input manifest, then compare the generated policy against the original tool inventory.

Risk: Mutable installation commands can fetch a different release than the one reviewed.

Mitigation: Install from a pinned commit or verified release and re-run review when upgrading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/gate-policy-generator)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON policy files and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local/offline execution; validation reports use rc=0/1/2 status behavior.]

## Skill Version(s):

1.0.0 (source: release metadata; artifact frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
