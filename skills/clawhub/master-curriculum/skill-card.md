## Description:

Guides agents to create sequenced Buddhist learning paths by matching a user's tradition and level to stage-by-stage study plans, source texts, recommended masters, and blind spots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan structured study across supported Buddhist traditions. It asks for tradition, current level, and practical constraints, then returns a staged curriculum with recommended texts, masters, goals, pitfalls, and follow-up routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Religious curriculum recommendations may be mistaken for formal practice instruction.

Mitigation: Present the output as educational study guidance and direct users to qualified teachers for formal practice guidance.

Risk: Source references or recommended masters may be incomplete or need independent verification.

Mitigation: Verify source references independently before relying on them, especially for formal study or publication.

Risk: A user may ask for an unsupported tradition and receive an unsuitable path if traditions are blended.

Mitigation: Use the artifact's fallback behavior: do not apply an unrelated curriculum, and suggest a relevant single-master skill or comparison workflow instead.

## Reference(s):

- [Chan Curriculum](references/chan.md)
- [Gelug Madhyamaka Curriculum](references/gelug-madhyamaka.md)
- [Huayan Curriculum](references/huayan.md)
- [Jingtu Curriculum](references/jingtu.md)
- [Sanlun / Zhongguan Curriculum](references/sanlun-zhongguan.md)
- [Theravada Vipassana Curriculum](references/theravada-vipassana.md)
- [Tiantai Curriculum](references/tiantai.md)
- [Weishi Curriculum](references/weishi.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown curriculum with staged sections, source-text references, recommended masters, blind spots, and extension routes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask follow-up questions for tradition, level, weekly time, language constraints, or access to a teacher before producing the curriculum.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
