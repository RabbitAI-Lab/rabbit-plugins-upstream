## Description:

Use when the user asks about Theravada, Pali sources, the Visuddhimagga, Buddhaghosa, Abhidhamma, Mahavihara commentarial interpretation, meditation-topic taxonomy, purification stages, or related Buddhist study topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to support Chinese-oriented study of Buddhaghosa, Theravada commentarial literature, Pali source citation, Visuddhimagga topic organization, and cautious doctrinal explanation. It is not a substitute for qualified meditation instruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate broadly for Theravada, Buddhist, Pali, or Buddhaghosa-adjacent questions.

Mitigation: Deploy it where this subject scope is expected, and review trigger behavior before using it in mixed-topic agent environments.

Risk: The skill may answer in a formal Chinese doctrinal style that is not suitable for every user.

Mitigation: Set host-agent language and audience expectations when needed, and review outputs for accessibility.

Risk: Users may treat doctrinal explanations as personal meditation instruction.

Mitigation: Keep the artifact's caution that formal practice guidance should come from a qualified teacher, and avoid individual attainment or practice-stage judgments.

Risk: Optional live retrieval can return untrusted text.

Mitigation: Treat retrieved text as citation data only, accept only declared source types and IDs, and fall back to offline sources if retrieval fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-buddhaghosa)
- [Teaching reference](artifact/references/teaching.md)
- [Voice reference](artifact/references/voice.md)
- [Source index](artifact/sources/INDEX.md)
- [Visuddhimagga excerpts](artifact/sources/visuddhimagga-excerpts.md)
- [SuttaCentral](https://suttacentral.net)
- [FoJin text search](https://fojin.app/api/search/content)
- [FoJin semantic search](https://fojin.app/api/search/semantic)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API Calls]

**Output Format:** [Markdown responses with inline source citations and optional retrieval links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese doctrinal style; citation requirements for doctrinal claims, practice guidance, and text interpretation.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/meta.json; artifact/SKILL.md frontmatter states 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
