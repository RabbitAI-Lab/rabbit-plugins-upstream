## Description:

Scans Chinese and English prompts for known jailbreak and dangerous-request patterns, then reports a risk tier and recommended handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code); All rights reserved (documentation and theory)

## Use Case:

Developers and security reviewers use this skill to screen agent prompts and user inputs for known jailbreak or dangerous-request patterns before launch or execution. Review flagged results before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad tool permissions could expose files or sensitive inputs beyond the intended scan.

Mitigation: Use explicit, authorized text or files and avoid supplying secrets unless necessary.

Risk: A pattern-based scan may miss unfamiliar attacks or flag benign text.

Mitigation: Treat results as screening guidance and have a person review consequential decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-redteam-kit)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text risk tier, matched patterns, and recommended action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The optional local scanner returns exit codes 0 (no known match), 1 (review), 2 (block), or 3 (input error).]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
