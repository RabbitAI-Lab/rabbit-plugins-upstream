## Description:

Execute independent phases with fresh implementation, review and test contexts. Resume from evidence and verify the combined result before closing a large change.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterflow-en](https://clawhub.ai/user/peterflow-en)

### License/Terms of Use:

MIT

## Use Case:

Developers and project coordinators use this skill to organize substantial software changes into bounded phases, assign implementation, review and testing work, resume from recorded evidence, and verify the combined feature before closing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's tool scope is undeclared, and a referenced path was missing from the scan bundle, leaving the security evidence incomplete.

Mitigation: Confirm referenced files exist before use and limit agent or tool access to the explicitly permitted workspace paths for each phase.

## Reference(s):

- [Role guide](artifact/references/roles.md)
- [Minimal-change review guide](artifact/references/minimal-change.md)
- [ClawHub skill page](https://clawhub.ai/peterflow-en/skills/implement-pro)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, JSON]

**Output Format:** [Markdown task and review guidance, with structured JSON review receipts when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include phase plans, role assignments, implementation changes, review receipts, and verification evidence.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
