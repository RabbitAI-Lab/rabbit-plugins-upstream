## Description:

Alibaba Cloud Simple Log Service (SLS) ingestion management for an already-deployed LoongCollector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to manage Alibaba Cloud SLS ingestion resources for an already deployed LoongCollector, including cloud-side onboarding, pipeline configuration, machine-group management, SLS Lens queries, and basic troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate Alibaba Cloud SLS resources through aliyun sls.

Mitigation: Install it only for workflows where agent-assisted SLS operations are intended, and review exact resource names and normalized diffs before approving writes.

Risk: Credential exposure could occur if AK/SK secrets are pasted into chat or printed from local configuration files.

Mitigation: Configure credentials outside the session, use credential-status checks only, and avoid pasting or displaying secret values.

Risk: Delete or cleanup actions can remove bindings or resources with high operational impact.

Mitigation: Treat cleanup as high-impact work and require explicit confirmation before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-loongcollector-ops)
- [Capability router](references/navigation.md)
- [Prerequisites](references/prerequisites.md)
- [RAM policies](references/ram-policies.md)
- [Risk and approval](references/risk-and-approval.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Verification method](references/verification-method.md)
- [Knowledge sources](references/knowledge-sources.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, configuration examples, and verification reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include approval prompts, normalized diffs, rollback notes, and validation results before cloud-side changes are executed.]

## Skill Version(s):

0.0.1-beta.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
