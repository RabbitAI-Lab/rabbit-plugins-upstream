## Description:

Research an open-ended question with current multi-source web evidence and produce a cited brief with facts, uncertainty, and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect current public web evidence for industry, policy, technology, company, or market questions and produce a cited decision brief with uncertainty and recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The live research path sends the research question and fetched URLs through Dataify and stores local evidence files.

Mitigation: Use it for appropriate public-information research and avoid sensitive or confidential prompts, URLs, and collected evidence.

Risk: Security evidence flags under-disclosed business-intelligence helper scripts and credential or preview handling risks.

Mitigation: Run only the documented live-research workflow unless the extra scripts have been reviewed for the intended inputs; keep API tokens in environment variables and never paste them into chat or logs.

Risk: The authoritative security verdict is suspicious pending review before installation.

Mitigation: Review the package and security guidance before installing or deploying it, especially in environments with sensitive data.

## Reference(s):

- [Dataify Documentation](https://doc.dataify.com)
- [Dataify Support](https://www.dataify.com/)
- [ClawHub Skill Page](https://clawhub.ai/dataify-server/skills/dataify-live-research)
- [Research Brief Contract](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief with numbered sources, JSON status and evidence files, and setup guidance when credentials are missing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN for live Dataify requests; stores resumable state, evidence, and report files locally.]

## Skill Version(s):

1.1.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
