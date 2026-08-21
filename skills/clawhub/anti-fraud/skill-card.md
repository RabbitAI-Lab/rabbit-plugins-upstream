## Description:

Anti-fraud helps agents classify suspicious messages, calls, links, apps, and transaction requests, produce risk-rated guidance, and run controlled anti-fraud education drills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

External users, families, and anti-fraud educators use this skill to identify common scam patterns, rate risk as red/yellow/green, produce practical safety guidance, and rehearse safer responses in training scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The training workflow can generate realistic scammer scripts and adaptive pressure lines that could be misused outside a controlled education setting.

Mitigation: Use the skill only for controlled anti-fraud training and defensive analysis; prefer red-flag annotation, safe response practice, and review of the roleplay workflow before use in a general assistant.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/ebandao777-oss/anti-fraud)
- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/anti-fraud)
- [Risk-level rules](references/risk-levels.md)
- [Scam knowledge base](references/scam-knowledge.md)
- [Emergency stop-loss SOP](references/emergency-sop.md)
- [Hallucination guard](references/hallucination-guard.md)
- [Anti-fraud drill workflow](workflows/anti-fraud-drill.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with risk labels, evidence summaries, checklists, warning cards, and training feedback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include red/yellow/green risk ratings, emergency action steps, family-support scripts, and controlled roleplay evaluation output.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
