## Description:

End-to-end functional testing framework for Huawei Cloud skills with a three-tier pipeline for single-skill testing, multi-skill orchestration, real-environment lifecycle checks, and consolidated reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to evaluate Huawei Cloud skills through repeatable phase-based tests, live cloud execution gates, orchestration checks, and final JSON and Markdown reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tester can execute untrusted tested-skill content with local and cloud credentials.

Mitigation: Run it only in an isolated workspace with a disposable Huawei Cloud account and narrowly scoped temporary credentials, and treat every skill under test as untrusted.

Risk: Live cloud write tests can create, update, or delete resources.

Mitigation: Keep ALLOW_WRITES=0 until generated commands are reviewed; enable writes only for approved cases and review cleanup output after the run.

Risk: Broad scans can test more installed or sibling Huawei Cloud skills than intended.

Mitigation: Prefer explicit --skills or --skill-path targets and use --no-siblings or sibling limits unless a broad scan is intentional.

Risk: Cloud credentials may be exposed if they are entered into chat or inline shell commands.

Mitigation: Configure AK/SK values out-of-band through the shell environment or Huawei Cloud profile and never paste secrets into the agent session.

## Reference(s):

- [Architecture](references/architecture.md)
- [Output Schema Specification](references/output-schema-spec.md)
- [Phase Transition Rules](references/phase-transition-rules.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Method](references/verification-method.md)
- [Phase Details](references/phase-details.md)
- [Agent Protocol](references/agent-protocol.md)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Huawei Cloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands plus generated JSON and Markdown test reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates phase-N summary JSON files and timestamped test-report.json/test-report.md files in sibling test-files directories; live writes are gated by ALLOW_WRITES.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
