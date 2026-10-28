## Description:

Uses Cue's remote research service to produce cross-checked reports from public financial, company, regulatory, and industry sources, with traceable source links and optional style imitation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and business users can use the skill to investigate public market, company, industry, and regulatory questions, compare entities, and produce source-linked research reports. They can optionally provide an authorized style reference to guide the report's writing style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an external runner, and its behavior may change between releases.

Mitigation: Review the runner and preferably pin the version before executing it.

Risk: Research queries and selected style-reference files are sent to Cue; local reference files may contain sensitive or restricted information.

Mitigation: Protect the Cue API key and upload only documents you are authorized to share.

Risk: Research consumes Cue service credits, and reports include Cue-hosted links.

Mitigation: Consider credit use before starting research and review hosted reports before sharing them.

## Reference(s):

- [Cue Deep Research on ClawHub](https://clawhub.ai/panting09266-ai/skills/cue-deep-research)
- [Cue service](https://cuecue.cn/)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-deep-research)
- [Cue runner repository (referenced by the skill)](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror (referenced by the skill)](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Structured Markdown research report with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research scope is supplied as a question; an optional URL or local style-reference document can guide writing style.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
