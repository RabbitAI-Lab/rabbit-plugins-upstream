## Description:

研林Skill — 产业投研日报生成器，将采集数据合成为完整券商级日报（Markdown格式）

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and course users use this skill to turn market, macro, news, and filing JSON inputs into a structured industry investment research daily report. The artifact states the report is for course teaching demonstration and is not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated investment research content could be mistaken for financial advice.

Mitigation: Use the report as course demonstration or research reference only, review source data and conclusions, and preserve the artifact's not-investment-advice disclosure.

Risk: Standalone mode depends on related Yanlin data-collection skills.

Mitigation: Prefer explicit JSON input paths; use standalone mode only when the related skills are installed and trusted.

Risk: The skill writes a local Markdown report to the selected output directory.

Mitigation: Choose an output directory that is appropriate for generated files and that the user is comfortable writing to.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/caoling7878-arch/skills/yanlin-report-gen)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown report file with JSON status on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads four user-provided JSON files by default and writes the report under the selected output directory and date.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
