## Description:

This skill helps knowledge workers, content teams, consultants, and creators turn local files, web research, and AI-HIVE content generation into supervised Claude Cowork projects with plans, permission boundaries, media tasks, and result indexes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan Claude Cowork-style workflows that combine authorized local files, web research, model routing, and AI-HIVE media or model tasks. It is intended to produce auditable project structure, approval gates, execution plans, task records, and result indexes rather than unsupervised generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE credentials could be exposed or sent to an untrusted endpoint.

Mitigation: Provide AI_HIVE_API_KEY only through a trusted environment and avoid overriding AI_HIVE_BASE_URL unless the endpoint is controlled and trusted.

Risk: Paid, batch, publishing, deletion, or account-access actions could be triggered without the user's intent.

Mitigation: Require explicit confirmation before any paid, batch, external publishing, deletion, or permission-expanding action runs.

Risk: The workflow may access files, webpages, accounts, or source material beyond the user's authorization.

Mitigation: Limit execution to explicitly authorized folders, webpages, accounts, and assets, and record approval gates in the plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-hot-claude-cowork-desktop)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [Claude Cowork product guide](https://claude.com/blog/the-claude-cowork-product-guide)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON execution-plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include model-routing recommendations, approval gates, task ledger fields, and local plan files for user review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
