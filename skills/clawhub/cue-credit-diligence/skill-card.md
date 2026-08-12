## Description:

This skill helps an agent run Cue-based credit due diligence research over public business, ownership, financial, operational, disclosure, and regulatory information, returning source-linked draft diligence material for credit risk and corporate screening workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Credit, risk, and business diligence users can use this skill to ask an agent to select and run an appropriate Cue research buddy for company profiling, corporate credit pre-diligence, financial diligence, or initial borrower screening. The output is supporting public-data research with source links, not a replacement for formal underwriting, legal review, or full diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can clone or update an external Cue runner before execution.

Mitigation: Confirm the Cue runner repository is trusted before installing or running the skill.

Risk: Research runs use the local Cue API key and consume Cue credits.

Mitigation: Require explicit user confirmation before each paid research run and avoid exposing local credentials in prompts or outputs.

Risk: The generated research is based on public-data support and may be incomplete for regulated credit decisions.

Mitigation: Keep source links in the report and route conclusions through formal diligence, legal, underwriting, or risk review before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-credit-diligence)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner repository on GitHub](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror on Gitee](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deep research runs consume Cue credits, may take several minutes, and require explicit user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
