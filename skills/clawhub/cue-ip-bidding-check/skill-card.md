## Description:

用 Cue 整合企业专利、软著、商标、资质许可、招投标与融资记录，帮助判断企业公开可见的技术能力与商业落地证据，并产出可复核的硬实力证据底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, procurement teams, and due-diligence reviewers use this skill to request company checks covering intellectual property, qualifications, bidding records, financing records, and source links. The skill is intended to deliver a structured Markdown evidence draft rather than a final legal or investment conclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an external Cue runner and API credentials, and the server security summary rates the release as suspicious because the runner is unpinned.

Mitigation: Review before installing, use a trusted pinned Cue runner version, verify its source, and protect ~/.cue/config.json and CUE_API_KEY as secrets.

Risk: Company names are passed into command-driven Cue research flows, which may expose sensitive targets or create command-construction risk if untrusted input is handled carelessly.

Mitigation: Avoid passing untrusted company names through shell-built commands; quote inputs carefully and review generated commands before execution.

Risk: The report depends on Cue service availability and external public data sources, so results can be incomplete, stale, or temporarily unavailable.

Mitigation: Retain source links, verify important claims against primary public sources, and treat the report as an evidence draft for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-ip-bidding-check)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Example Cue report](https://cuecue.cn/share/buddy-template-063fa4f79b2c)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and optional shell commands for running Cue and converting the report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected report sections include intellectual property lists, qualification checks, bidding analysis, financing records, technical capability assessment, commercialization evidence, and source links.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
