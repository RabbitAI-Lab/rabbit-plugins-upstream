## Description:

Diagnoses whether Chinese creator content gives audiences a clear takeaway and action impulse, with modes for draft review, viral-post decoding, and testing whether a hunch reflects a broader pattern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to diagnose whether a draft, viral reference, or raw hunch will leave an audience with one clear takeaway and a reason to save, share, comment, or follow. It is aimed at solo knowledge creators who need direct content-structure guidance they can act on themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local zmm convention and memory files and save user corrections or engagement lessons for later sessions.

Mitigation: Review where the vault resolves before installing, keep memory private, inspect it periodically, and avoid storing sensitive drafts or instruction-like corrections there.

Risk: Persistent local memory may carry stale or overly broad content-coaching assumptions into later sessions.

Mitigation: Inspect memory entries periodically and keep only concrete, non-sensitive corrections or validated engagement lessons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-resonate)
- [规则卡](artifact/references/规则卡.md)
- [Evaluation samples](artifact/evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown diagnostic report with quoted evidence labels and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Judgements are tied to source text and labelled as evidence, inference, or to-verify.]

## Skill Version(s):

0.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
