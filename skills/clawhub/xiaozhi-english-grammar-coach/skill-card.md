## Description:

英语语法教练：用追问帮初中生自己发现语法错误，并在同意后记录语法弱项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill to analyze short English grammar samples, guide learners through Socratic correction, and generate consent-gated grammar weakness tracking. It focuses on upper-primary and junior-middle-school grammar issues such as tense, subject-verb agreement, articles, prepositions, relative clauses, and sentence structure.

### Deployment Geography for Use:

Global, with localization required before student use outside the Chinese-language, China-mainland K12 context.

## Known Risks and Mitigations:

Risk: The skill asks minors for unrestricted writing samples and the security review says the main workflow does not activate the bundled crisis-safety protocol before student text intake.

Mitigation: Add the crisis exception directly to the main workflow before any intake, stop grammar coaching on self-harm, abuse, bullying, severe hopelessness, or family-safety disclosures, and follow the referral flow.

Risk: The skill is designed around Chinese-language, China-mainland K12 assumptions, including curriculum, consent expectations, and emergency-help channels.

Mitigation: Localize language, curriculum alignment, consent and guardian requirements, and emergency or youth-support channels before deploying outside that context.

Risk: The skill can record grammar weakness profiles for students when profile tracking and cross-skill sharing are enabled.

Mitigation: Require explicit profile, sharing, and guardian consent where applicable; provide view, correction, deletion, pause, sharing-control, and export paths for the grammar profile.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-grammar-coach)
- [英语错因维度表](references/english-error-dimension-table.md)
- [五类语法错误详细分析与追问话术扩展库](references/grammar-patterns.md)
- [危机例外](shared/crisis-exception.md)
- [危机识别与转介协议](shared/crisis-referral-protocol.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [全库统一词表](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown-style conversational text with short analyses, guided questions, practice prompts, and optional profile-update payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained to brief student-facing coaching turns and consent-gated tracking summaries; no shell commands or code execution are produced.]

## Skill Version(s):

2.1.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
