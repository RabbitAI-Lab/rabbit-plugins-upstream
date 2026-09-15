## Description:

用 Cue 整合企业专利、软著、商标、资质许可、招投标与融资记录，判断公开可见的技术能力与商业落地证据并产出可复核的硬实力证据底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run Cue-based due diligence on a target company before bidding, supplier onboarding, technical diligence, or commercialization assessment. It focuses on public evidence for intellectual property, qualifications, bidding records, financing history, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends company names, due-diligence questions, and Cue account credentials to Cue-controlled services.

Mitigation: Use it only when that data can be shared with Cue, avoid confidential targets where inappropriate, and review account credential handling before execution.

Risk: The workflow defaults to returning a Cue share link that may be forwarded beyond the original user.

Mitigation: Ask the agent not to include a share link for confidential work and only distribute generated links to intended recipients.

Risk: Credit, referral, and payment prompts appear in the workflow and can be confused with research findings.

Mitigation: Treat billing and referral text as vendor account guidance, separate from the due-diligence result.

Risk: Research quality depends on Cue services and external public data sources.

Mitigation: Review the generated report, preserve source links, and manually verify important claims through authoritative public sources when decisions depend on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-ip-bidding-check)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue service health endpoint](https://cuecue.cn/api/health)
- [CNIPA manual fallback source](https://www.cnipa.gov.cn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source links and optional shell commands for Cue execution and conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Cue share link and local report path when the external runner returns a valid conversation id.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
