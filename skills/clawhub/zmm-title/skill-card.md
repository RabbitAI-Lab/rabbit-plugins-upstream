## Description:

Helps creators generate and evaluate multi-platform titles and cover text by choosing content-fit title structures, checking red lines, and explaining each recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and content operators use this skill to produce Douyin, Xiaohongshu, WeChat Channels, and public-account titles or cover text for a draft or topic, with structure labels and red-line checks. It is aimed at individual knowledge creators who need concise options plus rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on local vault rules that are not packaged with the release, so red-line checks may be unavailable in a fresh environment.

Mitigation: Confirm the referenced zmm vault/framework files are present before use; if they are missing, treat output as incomplete and avoid relying on red-line claims.

Risk: The skill automatically writes title preferences and feedback into memory, which may retain user style choices across sessions.

Mitigation: Review or disable memory write-back when persistent preference storage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-title)
- [标题结构库](references/标题结构库.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured title candidates, rationale, red-line status, Top 3 recommendations, and short cover-text options.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask one clarifying question when platform, topic, or audience is missing.]

## Skill Version(s):

0.2.4 (source: server release evidence; artifact frontmatter lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
