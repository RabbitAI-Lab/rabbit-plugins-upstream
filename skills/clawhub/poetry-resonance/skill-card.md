## Description:

诗遇 Poetry Resonance helps users connect Tang and Song poetry with daily life through poem matching, plain-language study notes, daily quote cards, and spaced-repetition recitation review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users and poetry learners use this skill to find relevant Chinese poetry for personal moments, produce concise social copy or study notes, receive daily poetry prompts, and review learned poems over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may store learning history in ~/.workbuddy/poetry-resonance/progress.json.

Mitigation: Use it only where local progress retention is acceptable; on shared machines, review or delete that file when learning history should not persist.

Risk: Poetry source versions can differ from commonly recognized public quotations.

Mitigation: Use the curated poem library for outward-facing quotations and treat the full Li Bai corpus as internal search and verification support.

Risk: The skill can help prepare notes or social copy that a user may save externally.

Mitigation: Confirm the destination before saving notes or copied text outside the local agent session.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Curated Li Bai poetry study library](artifact/references/poems.md)
- [Li Bai source corpus metadata](artifact/references/libai_raw.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown prose with structured poetry recommendations, study notes, daily card text, review prompts, and optional local progress configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use a local progress file at ~/.workbuddy/poetry-resonance/progress.json for learning history.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
