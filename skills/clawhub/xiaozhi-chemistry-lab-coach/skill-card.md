## Description:

化学实验探究教练帮助中文 K12 学生理解化学实验装置选择、操作顺序、现象与结论区分、检验与除杂方案，以及初中必做实验和高中必修起点实验的备考要点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 students use this skill to reason through chemistry experiment questions, explain why apparatus and operations are chosen, prepare for lab-operation exams, and distinguish observations from conclusions. It is also useful for supervised classroom review where safety rules and consent-gated student profile memory are acceptable.

### Deployment Geography for Use:

Global; deployments outside mainland China should localize language, curriculum assumptions, emergency contacts, and minor-consent rules before use.

## Known Risks and Mitigations:

Risk: Students may ask for chemistry experiment steps, quantities, or shortcuts that could be unsafe outside a supervised lab.

Mitigation: The skill refuses home-operation instructions for risky experiments, gives principles or safer study alternatives, and follows shared lab safety rules for demonstrations, accidents, and required protective practices.

Risk: Student profile memory and cross-skill handoffs can expose learning records or preferences if enabled without clear consent.

Mitigation: The skill defaults to session-only tutoring and requires explicit consent for profile use, writeback, sharing, reminders, viewing, correction, deletion, pausing, and export.

Risk: K12 crisis or safety disclosures can exceed the scope of chemistry tutoring.

Mitigation: The skill stops normal tutoring on crisis signals, explains AI boundaries, directs the student to a trusted adult, and uses location-appropriate emergency guidance.

Risk: Deployments outside mainland China may have different emergency numbers, curriculum scope, language expectations, and minor-consent rules.

Mitigation: Deployment guidance requires localizing emergency contacts, curriculum assumptions, language, and consent policies before use outside mainland China.

## Reference(s):

- [Chemistry Lab Guide](artifact/references/chemistry-lab-guide.md)
- [Lab Safety](artifact/shared/lab-safety.md)
- [Crisis Exception](artifact/shared/crisis-exception.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)
- [DNA Profile Schema](artifact/shared/dna-profile.schema.json)
- [Handover Protocol Schema](artifact/shared/handover-protocol.schema.json)
- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-lab-coach)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown conversational tutoring guidance with structured handoff/profile data when consented]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Safety-first chemistry lab coaching; consent-gated profile memory and cross-skill handoffs; no hidden code execution, persistence, or exfiltration found in security evidence.]

## Skill Version(s):

2.2.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
