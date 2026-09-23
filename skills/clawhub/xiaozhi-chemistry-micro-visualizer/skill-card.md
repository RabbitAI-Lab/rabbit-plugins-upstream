## Description:

This skill helps Chinese K12 chemistry learners explain observable phenomena through particle-level models, bounded analogies, and text-based molecular diagrams for molecules, atoms, ions, chemical change, conservation of mass, dissolution, ionization, and redox basics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, educators, and tutoring agents use this skill to teach chemistry concepts by moving between observed phenomena, particle diagrams, and symbolic explanations. It is intended for Chinese-language K12 chemistry support, mainly junior-high chemistry and high-school required-course introductions.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, minor privacy rules, guardian-consent handling, and crisis referral channels before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill assumes a Chinese-language K12 chemistry context and China-mainland support channels.

Mitigation: Before use elsewhere, localize curriculum alignment, privacy and guardian-consent requirements, and crisis referral resources.

Risk: The skill may read chemistry profile weaknesses when long-term profile memory is enabled.

Mitigation: Read profile data only after explicit profile consent and current-session agreement; honor view, correction, deletion, pause, sharing-control, and export requests.

Risk: Chemistry explanations can drift into unsafe experiment instructions.

Mitigation: Keep dangerous experiments to principle-level explanation or school-lab observation; do not provide home procedures for heating, chemical mixing, gas generation, or other hazardous operations.

Risk: Student crisis signals can appear during tutoring interactions.

Mitigation: Stop normal tutoring on crisis signals, avoid diagnosis, contact trusted adults, and provide emergency guidance only for the confirmed region.

Risk: Students may ask for help during active exams or restricted assessments.

Mitigation: Do not solve, hint, or guide active exam questions; invite the student to return after the assessment for review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-micro-visualizer)
- [ClawHub Publisher Profile](https://clawhub.ai/user/qizhitang)
- [Chemistry Micro Analogy Bank](artifact/references/chemistry-micro-analogy-bank.md)
- [Learning DNA Profile Schema](artifact/shared/dna-profile.schema.json)
- [Platform Conventions](artifact/shared/platform-conventions.md)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)
- [Lab Safety Guidance](artifact/shared/lab-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Chinese-language tutoring guidance with inline text diagrams and short Markdown tables or lists when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read consent-gated chemistry profile fields when enabled; does not write profile records.]

## Skill Version(s):

2.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
