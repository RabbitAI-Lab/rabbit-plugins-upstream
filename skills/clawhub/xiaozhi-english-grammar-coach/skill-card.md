## Description:

A Chinese-language K12 English grammar coaching skill that uses guided questions to help students identify grammar errors and, with consent, track recurring grammar weaknesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-speaking K12 learners, parents, teachers, or learning agents use this skill to coach English grammar through Socratic prompts, focused practice, and consent-gated weakness tracking.

### Deployment Geography for Use:

Global; operators outside mainland China should localize language, curriculum assumptions, crisis resources, and minor-consent requirements.

## Known Risks and Mitigations:

Risk: The skill is intended for K12 learners and can involve minors' learning profiles.

Mitigation: Deploy with local minor-consent rules, parent or teacher involvement for younger learners, and the skill's consent checks before any profile update.

Risk: Crisis or safety disclosures can occur during tutoring even though the skill is not a counseling tool.

Mitigation: Follow the bundled crisis exception and referral protocol, stop normal coaching, and route the user to trusted adults and local emergency resources.

Risk: Using the skill during an active exam or test could undermine assessment integrity.

Mitigation: Follow the artifact behavior that withholds hints or answers during exams and offers post-exam review instead.

Risk: The skill's language, curriculum assumptions, and crisis resources are Chinese-market oriented.

Mitigation: Localize content, curriculum expectations, consent requirements, and crisis-resource references before deploying in other jurisdictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-grammar-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [English error dimension table](references/english-error-dimension-table.md)
- [Grammar patterns](references/grammar-patterns.md)
- [AI item check](shared/ai-item-check.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Grade bands](shared/grade-bands.md)
- [Hint ladder](shared/hint-ladder.md)
- [Platform conventions](shared/platform-conventions.md)
- [Vocabulary and profile rules](shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Conversational text and Markdown coaching guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose consent-gated learning profile updates and handoff payloads; does not include executable code.]

## Skill Version(s):

2.3.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
