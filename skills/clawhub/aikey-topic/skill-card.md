## Description:

Helps solo knowledge creators choose short-video topics by testing audience demand against comparable content signals and their own evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Solo knowledge creators use this skill to explore short-video topics, assess a proposed topic, or find a compelling angle before deciding what to film.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local content history and other potentially private vault material.

Mitigation: Use a dedicated workspace and avoid granting access to unrelated private notes or business records.

Risk: The skill may run local scripts and automatically write feedback or topic decisions into persistent framework and memory files without clear approval boundaries.

Mitigation: Review proposed commands and file diffs before accepting write-backs.

## Reference(s):

- [Topic selection approaches](references/选题三路.md)
- [Finding a compelling angle](references/找拉力.md)
- [Question exploration and audience resonance](references/问题探寻与共鸣.md)
- [Topic assessment rules](references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational Markdown and topic-pipeline notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers evidence-tagged topic candidates or a single-topic assessment; may update local topic and memory files.]

## Skill Version(s):

0.5.4 (source: ClawHub release metadata; artifact frontmatter lists 0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
