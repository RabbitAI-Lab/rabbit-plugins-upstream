## Description:

用 Cue 整合企业专利、软著、商标、资质许可、招投标与融资记录，判断公开可见的技术能力与商业落地证据，产出可复核的硬实力证据底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, investment, supplier-risk, and technical due-diligence users use this skill to investigate a target company's public patents, software copyrights, trademarks, licenses, bidding history, financing records, and evidence of commercial execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target company names, investigation scope, and generated reports may contain sensitive due-diligence information and are sent to Cue and saved locally.

Mitigation: Use an appropriate Cue account and dedicated API key, limit submitted details to the investigation scope, and handle saved reports as sensitive files.

Risk: The workflow depends on external Cue services, external data sources, and a referenced runner outside the packaged artifact.

Mitigation: Review the runner source before setup, verify Cue connectivity before use, and preserve source links in the final report so findings can be checked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-ip-bidding-check)
- [Cue report example](https://cuecue.cn/share/buddy-template-063fa4f79b2c)
- [Cue service](https://cuecue.cn)
- [Cue runner source referenced by skill](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by skill](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source links, plus shell commands and optional document-conversion guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs one Cue research template for a target company and saves a local report.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
