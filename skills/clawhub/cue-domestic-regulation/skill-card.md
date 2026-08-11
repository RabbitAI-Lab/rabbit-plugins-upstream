## Description:

国内法规调研 helps agents research Chinese domestic laws, administrative regulations, and enforcement materials, then organize legislative background and compliance points with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, and legal researchers use this skill to request Chinese domestic regulation research through Cue and receive a sourced Chinese report covering applicable rules, legislative background, compliance obligations, enforcement practice, and official source links.

### Deployment Geography for Use:

Global; the research scope is Chinese domestic regulation and public Chinese legal and government sources.

## Known Risks and Mitigations:

Risk: Research questions are sent to cuecue.cn under the user's Cue account.

Mitigation: Redact confidential, privileged, personal, and non-public business information before use.

Risk: The skill depends on an external Cue runner and Cue service availability.

Mitigation: Verify the runner source before installation and run the documented health checks before each research task.

Risk: Generated reports support legal research but are not legal advice.

Mitigation: Review cited source links and consult qualified counsel before relying on the report for legal or compliance decisions.

Risk: Research reports are written to local storage.

Mitigation: Store generated reports in locations appropriate for their sensitivity and apply the user's normal document handling controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-domestic-regulation)
- [Cue API key](https://cuecue.cn/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)
- [Ministry of Justice of China](https://www.moj.gov.cn)
- [State Council of China](https://www.gov.cn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese Markdown report with source links, plus shell commands and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved locally under the configured output path; legal conclusions should be reviewed against the cited sources.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
