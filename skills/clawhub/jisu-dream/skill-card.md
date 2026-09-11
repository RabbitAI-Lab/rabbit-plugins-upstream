## Description:

按关键词检索周公解梦释义，支持分页，适用于回答梦见蛇、梦到飞或类似解梦问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Duke of Zhou dream interpretations by keyword through JisuAPI. Agents can summarize the returned entries for conversational dream-interpretation questions while reminding users that results are for entertainment or learning reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends dream keywords and an API key to JisuAPI when invoked.

Mitigation: Avoid entering highly sensitive personal details in dream keywords and keep JISU_API_KEY in environment or secret management rather than hardcoding it.

Risk: Dream-interpretation results could be mistaken for practical, medical, or other real-world decision guidance.

Mitigation: Present results as entertainment or learning reference and avoid treating them as advice for real-world decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jisuapi/skills/jisu-dream)
- [JisuAPI Dream API Documentation](https://www.jisuapi.com/api/dream)
- [JisuAPI Provider Site](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON API results and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; sends dream keywords to JisuAPI for lookup.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
