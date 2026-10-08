## Description:

Scans untrusted text for English and Chinese prompt-injection patterns and suggests whether to pass, quarantine, or drop it before it enters an agent's context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); all rights reserved (documentation and theoretical text)

## Use Case:

Developers and agent operators use this skill to screen web pages, email, retrieval results, and other external text for prompt-injection attempts before supplying them to an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote install commands fetch code from outside the workspace.

Mitigation: Verify the source you intend to trust and review the install command before running it.

Risk: Scanning unnecessary sensitive files may expose their contents to the local workflow.

Mitigation: Scan only content needed for the task and avoid supplying unnecessary sensitive files.

Risk: Pattern-based screening may miss an attack or flag harmless text.

Mitigation: Keep external content untrusted and review consequential pass, quarantine, or drop decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-shield)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk score (0–100), matched rules, and suggested pass, quarantine, or drop action.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
