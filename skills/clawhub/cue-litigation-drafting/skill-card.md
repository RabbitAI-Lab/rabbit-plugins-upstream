## Description:

根据用户提供的案件事实、当事人立场和材料，通过 Cue 服务端生成中文诉讼文书草稿，并附法条和类案依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External legal professionals and agents use this skill to draft Chinese litigation documents such as complaints, answers, evidence objections, appeal documents, attorney letters, and evidence lists from case facts and party positions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Case facts, party information, and uploaded opposing-party materials are sent to Cue's remote service.

Mitigation: Confirm the user is allowed to send those materials to Cue before use, and avoid privileged or confidential material unless applicable legal, client, and organizational rules permit it.

Risk: Generated litigation documents are drafts and may contain legal, factual, citation, or formatting issues.

Mitigation: Require review and adjustment by a qualified lawyer, including independent verification of statutes, case references, evidence descriptions, and final filing format.

Risk: The skill depends on Cue service availability and public legal data sources.

Mitigation: Run the documented Cue health check before use, retry later during service issues, and use official legal databases or other documented fallback sources when Cue is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-litigation-drafting)
- [Cue platform](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/api-key)
- [Cue service health endpoint](https://cuecue.cn/api/health)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Court Litigation Service Network](https://ssfw.court.gov.cn)
- [PKULaw](https://www.pkulaw.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown legal document draft with supporting shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated documents require qualified legal review; case facts and uploaded materials are sent to Cue's remote service.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter shows 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
