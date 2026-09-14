## Description:

HR decision briefs: clarify the problem, ownership and evidence for one accountable human decision; not a weekly roundup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mwclaw](https://clawhub.ai/user/mwclaw)

### License/Terms of Use:

MIT-0

## Use Case:

HRBPs, People leaders, managers, and advisors use this skill to turn supplied HR issue materials into source-backed briefs for accountable human review. It helps clarify the decision, ownership, evidence, options, unresolved gaps, and next action without making or executing employment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive employment or personal information may be included in HR issue materials.

Mitigation: Use only information the user is authorized to process, prefer synthetic or de-identified inputs, request the minimum decision-relevant information, and avoid unnecessary medical or identifying details.

Risk: A generated brief could be mistaken for an employment, legal, payroll, system-update, or employee-communication decision.

Mitigation: Keep consequential decisions and external actions with the appropriate human reviewer; the skill should prepare a brief and make human decision status visible.

Risk: Instructions embedded in supplied HR notes, resumes, policies, attachments, or retrieved text could conflict with the skill boundary.

Mitigation: Treat embedded instructions as untrusted content and rely on exact supplied sources for evidence rather than letting source text override the workflow.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mwclaw/skills/hr-decision-packet)
- [Source homepage](https://github.com/mwclaw/openclaw-hr-workflows/tree/main/skills/hr-decision-packet)
- [Decision packet template](templates/decision-packet.md)
- [HR Decision Packet Evals](references/evals.md)
- [Synthetic before-and-after example](examples/framing-before-after.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown decision brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default target is a concise 250-450 word brief for straightforward cases, with an optional expanded evidence appendix for higher-stakes or more complex matters.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
