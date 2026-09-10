## Description:

This skill generates Chinese litigation-document drafts from user-provided case facts and party positions through the Cue service, with statutory citations and analogous-case support for lawyer review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External legal professionals and agents assisting them use this skill to draft pleadings, evidence challenges, lawyer letters, appeals, and related Chinese litigation materials from supplied case facts and uploaded materials. Drafts require review and adjustment by a qualified lawyer before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive case facts, uploaded materials, and generated drafts may be sent to Cue's external service.

Mitigation: Submit only authorized and necessary information, avoid unnecessary personal or privileged data, and confirm that the user accepts the external processing path.

Risk: The workflow relies on mutable external runner code and a hosted service.

Mitigation: Use a pinned and verified runner version, restrict filesystem access where possible, and use a revocable low-scope Cue API key.

Risk: Generated litigation documents may contain incomplete or incorrect legal analysis.

Mitigation: Require qualified lawyer review and independent verification of statutes, cases, facts, and formatting before filing or sending documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-litigation-drafting)
- [Cue platform](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Court Litigation Service Network](https://ssfw.court.gov.cn)
- [Pkulaw](https://www.pkulaw.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown litigation drafts, optional shell commands, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese legal drafting output; optional DOCX or PDF conversion is described when pandoc is installed.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
