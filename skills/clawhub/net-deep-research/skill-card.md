## Description:

Performs deep multi-source internet research for complex web truth-finding tasks, with explicit activation preferred and automatic activation limited to complex verification or research needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[h4444433333](https://clawhub.ai/user/h4444433333)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, analysts, and employees use this skill when a question requires deep online verification, cross-source fact checking, authenticity checks, or complex web research beyond routine lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deep research runs may send research-source metadata, structured claims and evidence snippets, query categories, confidence, and usefulness signals to shoggoth.vip.

Mitigation: Install only if that data sharing is acceptable for the intended environment and avoid using the skill for confidential research unless policy allows it.

Risk: Explicit diagnostic or vote modes may send raw query text, full answer text, or trust and untrust votes.

Mitigation: Use those modes only when the user intentionally requests them and the additional disclosure is appropriate.

Risk: The skill can produce misleading conclusions if source evidence is stale, conflicting, or insufficient.

Mitigation: Review cited sources, stated uncertainties, and cross-source conflict notes before relying on the answer for consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/h4444433333/skills/net-deep-research)
- [Feedback Contract](references/feedback-contract.md)
- [Research Playbook](references/research-playbook.md)
- [Source Scoring](references/source-scoring.md)
- [Writing Rules](references/writing-rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown research answer with cited sources, uncertainty notes, and an explanation of source confidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include verified facts, inference, cross-source notes, source reputation signals, and uncertainty limits depending on the research question.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact _meta.json lists 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
