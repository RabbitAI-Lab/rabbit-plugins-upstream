## Description:

This skill helps advertising and growth teams diagnose ad fatigue from campaign signals, preserve effective creative variables, replace fatigued elements, and prepare refreshed scripts, prompts, commands, and AI-HIVE generation batches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External advertising operators, growth teams, brand creative teams, and content operations teams use this skill to turn historical media, performance metrics, product facts, channel constraints, and budget limits into an auditable ad-fatigue diagnosis and creative refresh plan. It can also prepare runnable AI-HIVE commands for authorized image or video generation after parameters, routing, and cost-sensitive choices are reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload prompts and media to an external AI-HIVE service.

Mitigation: Upload only assets the user is authorized to use, review prompts before submission, and avoid sensitive or unauthorized media.

Risk: Image or video generation may incur AI-HIVE costs.

Mitigation: Confirm prompts, routing mode, model choices, and price snapshots before running generation commands; use a small sample before batch generation.

Risk: The workflow depends on an AI-HIVE API key.

Mitigation: Store the key in an environment variable or protected config file, avoid logging or echoing it, and keep local config permissions restricted.

Risk: Generated ad claims or fatigue diagnoses may be inaccurate without reliable performance data and product facts.

Mitigation: Mark unverifiable claims for review, validate product and platform facts with authoritative sources, and avoid promises about traffic, conversion, ranking, approval, or return on investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ad-fatigue-refresh-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with ordered sections, inline shell commands, optional JSON files, and generated task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing mode, model or price snapshot, taskId, task status, local file paths, and acceptance-check results when generation is used.]

## Skill Version(s):

1.0.0 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
