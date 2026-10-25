## Description:

小红书文案创作 helps creators and content teams search recent viral Xiaohongshu notes, analyze content patterns, and generate publish-ready note copy with titles, body text, tags, and source formulas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[if530770](https://clawhub.ai/user/if530770)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content operators, brand teams, and new media practitioners use this skill to generate Xiaohongshu-ready copy from keyword-based viral note retrieval, pattern analysis, optional style samples, and recent topic material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and contacts redfox.hk for Xiaohongshu note data.

Mitigation: Use a scoped and revocable REDFOX_API_KEY, avoid hardcoding it, and confirm the key source and permissions before use.

Risk: The workflow can use personal writing samples to imitate a user's style.

Mitigation: Avoid providing sensitive personal samples and review generated copy before publishing.

Risk: The script creates a local HTML report and security evidence notes that this behavior may overwrite files or include unsafe HTML content.

Mitigation: Run the skill in a restricted working directory and review or patch HTML output behavior so it is opt-in, path-contained, non-overwriting, and properly escaped.

## Reference(s):

- [Xiaohongshu Hot Article Data Format](artifact/references/xhs_hot_article_format.md)
- [RedFoxHub](https://redfox.hk)
- [ClawHub Skill Page](https://clawhub.ai/if530770/skills/xhs-copywriter)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Text, Shell commands, Configuration]

**Output Format:** [Markdown sections with generated copy, tags, viral formula analysis, and cited reference note links; supporting script output is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY for RedFox API access and may use web search for recent Xiaohongshu topic material.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
