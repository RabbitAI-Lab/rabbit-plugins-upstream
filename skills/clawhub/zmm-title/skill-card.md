## Description:

詹明明·标题与封面 helps agents create platform-specific Chinese social-media titles and cover text by matching title structures to the content, checking red-line constraints, and explaining the structure choice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to generate or refine Chinese social-media titles, cover text, and upload copy for platforms such as Douyin, Xiaohongshu, WeChat Channels, and public accounts. The skill returns candidates with structure labels, fit rationale, and red-line checks, and can advise whether a draft opening should change to match the chosen title.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may write ordinary user feedback into long-term shared writing memory without explicit approval.

Mitigation: Use it where memory writes are reviewed or disabled, or require confirmation before persistent memory updates.

Risk: Shared vault content read or written by the skill can influence future copywriting behavior.

Mitigation: Treat shared vault content as editable agent state and review it before relying on it as policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-title)
- [标题结构库](artifact/references/标题结构库.md)
- [规则卡](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured title candidates, cover-text options, rationale, and red-line status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform, topic, audience, title structure IDs, content-shape notes, selected title recommendations, and memory-update guidance.]

## Skill Version(s):

0.2.8 (source: server release evidence; artifact frontmatter lists 0.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
