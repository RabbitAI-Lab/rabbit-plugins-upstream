## Description:

The skill helps agents route Alibaba Cloud AgentLoop requests for observability onboarding, Dataset management, pipeline building, evaluation, and stored experience recall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and operations engineers use this skill to guide AgentLoop cloud workflows across application observability onboarding, Dataset lifecycle work, data pipelines, evaluation tasks, and experience recall. It is intended for users who can review and authorize Alibaba Cloud CLI operations under their own cloud identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change local and Alibaba Cloud environments while operating AgentLoop resources with the user's cloud identity.

Mitigation: Install and use it only when that level of AgentLoop operation is intended, and review proposed CLI or configuration changes before execution.

Risk: The security review notes an unsafe automatic CLI installer path.

Mitigation: Avoid `curl | bash`; review CLI install or upgrade steps through an approved process before running them.

Risk: Recall, preview, AI pipeline nodes, and global dedup flows can send task, row, or processing data outward.

Mitigation: Require explicit approval before outbound recall or preview, and avoid these flows for secrets, PII, or regulated data unless retention and provider controls are approved.

Risk: Cloud credentials, APM license keys, or ContextStore API keys could be exposed in chat or logs if mishandled.

Mitigation: Keep credentials out of chat and logs, report only status or variable names, and rely on configured identities rather than pasted secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-agentloop-management)
- [AgentLoop Skill Router](artifact/SKILL.md)
- [Application Onboarding](artifact/references/onboarding.md)
- [Application Monitoring](artifact/references/apm.md)
- [AI Observability](artifact/references/ai.md)
- [Dataset Management](artifact/references/dataset/dataset.md)
- [Evaluation](artifact/references/evaluation/evaluation.md)
- [Pipeline](artifact/references/pipeline/pipeline.md)
- [Experience Recall](artifact/references/experience/experience.md)
- [RAM Policies](artifact/references/ram-policies.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, JSON examples, and generated code or command files when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include proposed Alibaba Cloud CLI commands, local wrapper-script invocations, configuration changes, verification steps, and redacted status summaries.]

## Skill Version(s):

0.1.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
