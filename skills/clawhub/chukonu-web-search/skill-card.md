## Description:

Guides agents in using the Chukonu remote MCP search and research tools to retrieve web, academic, patent, and Chinese legal or regulatory evidence for cited answers, fact checks, prior-art review, PDF-focused research, and multi-turn research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hhhwor](https://clawhub.ai/user/hhhwor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure OAuth access to the Chukonu search MCP and to guide search, research, citation, legal evidence handling, and result-limitation disclosure workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and research objectives are sent to a third-party remote MCP service.

Mitigation: Confirm trust in the Chukonu service before installation and avoid submitting sensitive information unless the deployment policy permits it.

Risk: Misconfigured static authorization headers or exposed tokens can cause authentication failures or credential leakage.

Mitigation: Use the documented OAuth flow with host-managed tokens, and do not place OAuth tokens in logs, examples, or manual Authorization headers.

Risk: Retrieved evidence, especially legal or time-sensitive material, may be partial, unavailable by public URL, stale, or insufficient for a definitive conclusion.

Mitigation: Check retrieval assessments, failures, legal status fields, dates, and coverage gaps, and disclose limitations before presenting conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hhhwor/skills/chukonu-web-search)
- [Chukonu remote MCP endpoint](https://search.houdutech.cn/web/mcp/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides remote MCP calls and evidence-grounded answers; it does not produce local executable payloads.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
