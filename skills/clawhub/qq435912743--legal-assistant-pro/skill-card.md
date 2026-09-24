## Description:

Comprehensive Chinese-law assistant for contract review, consumer protection, labor disputes, family and property matters, intellectual property basics, traffic incidents, lending disputes, and online rights guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill for informational guidance on common Chinese-law scenarios, including reviewing contract risks, planning dispute-resolution steps, identifying evidence to collect, and understanding relevant legal procedures. The skill states that its outputs are for reference and general legal education, not formal legal advice.

### Deployment Geography for Use:

Global for Chinese-law informational use cases

## Known Risks and Mitigations:

Risk: Users may treat informational Chinese-law guidance as formal legal advice.

Mitigation: Keep the legal-education disclaimer visible, avoid presenting outputs as legal opinions, and direct users with specific or high-stakes matters to a licensed lawyer or appropriate authority.

Risk: The learner can persist cross-session preferences, errors, and notes in learned_patterns.json, which may capture sensitive legal facts or personal identifiers.

Mitigation: Disable or remove the learner unless persistent storage is explicitly required, and do not store legal facts, personal identifiers, dispute details, or private preferences in the learning file.

Risk: The artifact describes automatic SKILL.md updates after repeated errors, which could change skill behavior without review.

Mitigation: Require human review and security scanning before accepting any changes to SKILL.md or other skill files.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown or plain text guidance, with occasional inline shell commands for the optional learner utility]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk ratings, evidence checklists, process steps, suggested wording, and learner insights when the optional learner is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
