## Description:

Generates personalized English listening practice for learners based on vocabulary level and interests, then helps identify whether listening difficulty comes from word meaning, sentence structure, or speed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners use this skill to practice English listening with short, level-matched materials, comprehension questions, vocabulary notes, and follow-up diagnosis of listening blockers. It is designed for Chinese K12 contexts, especially upper-primary and middle-school English practice.

### Deployment Geography for Use:

China mainland by default; localize crisis contacts, school-level assumptions, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can use learning, vocabulary, and interest profile data to personalize listening practice.

Mitigation: Confirm profile, guardian, and cross-skill sharing consent before enabling persistent personalization or profile writeback.

Risk: The skill is designed around Chinese K12 assumptions, including school levels, curriculum alignment, and default crisis contacts.

Mitigation: Localize emergency contacts, curriculum assumptions, and minor-consent requirements before deploying outside mainland China.

Risk: Listening practice may degrade to text or reading-style exercises when voice synthesis, speech transcription, or statistics capabilities are unavailable.

Mitigation: Tell learners when a session is no longer true listening practice, avoid phoneme-level pronunciation judgments without speech scoring, and avoid historical progress claims without platform statistics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-listening-trainer)
- [qizhitang publisher profile](https://clawhub.ai/user/qizhitang)
- [Listening topic templates](artifact/references/listening-topic-templates.md)
- [English error dimension table](artifact/shared/english-error-dimension-table.md)
- [Platform conventions and degradation paths](artifact/shared/platform-conventions.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown conversational guidance with generated listening passages, comprehension questions, vocabulary notes, learner feedback, and consent-gated profile handoff examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce short English listening passages, Chinese learner-facing explanations, diagnostic summaries, and profile-control prompts.]

## Skill Version(s):

2.1.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
