## Description:

Provides multi-platform title and cover-text guidance that selects content-fit title structures, explains the rationale for each option, and checks titles against stated red lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to generate or improve platform-specific social titles and cover text for Douyin, Xiaohongshu, video accounts, and public-account publishing. It is designed to explain which title structure is being used, why it fits the content, and whether the result passes the skill's red-line checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read a local zmm/vault knowledge base and persist title feedback automatically.

Mitigation: Install only where that local access is acceptable, and review or disable the memory/framework write-back behavior when per-request control is required.

Risk: The skill depends on local reference and memory files for red-line and workflow checks.

Mitigation: Confirm the expected local references are present before relying on red-line guarantees; if they are unavailable, treat the output as incomplete.

## Reference(s):

- [标题结构库](artifact/references/标题结构库.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-title)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with title candidates, structure labels, rationale, red-line status, top recommendations, and short cover-text options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask for missing platform, topic, or audience context before producing final title recommendations.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
