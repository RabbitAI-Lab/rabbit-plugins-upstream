## Description:

Scans Chinese and English prompts for known jailbreak and dangerous-action patterns, reports risk tiers, and helps gate high-risk requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this local scanner to check agent prompts and incoming requests for known jailbreak and dangerous-action patterns before deployment or execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pattern matching can miss unfamiliar attacks or misclassify a request.

Mitigation: Treat the local scanner as a heuristic aid, not a replacement for human review or broader security testing.

Risk: Installing an unverified package or relying on scanner results alone can undermine review.

Mitigation: Verify the package source before installation and have a reviewer assess flagged requests and consequential decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-redteam-kit)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance and plain-text scanner results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanner exit codes: 0 no known pattern, 1 human review, 2 block, 3 usage error.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
