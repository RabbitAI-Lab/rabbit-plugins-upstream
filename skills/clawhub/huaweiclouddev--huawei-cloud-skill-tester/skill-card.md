## Description:

End-to-end functional testing framework for Huawei Cloud skills, covering single-skill testing, multi-skill orchestration, full-flow real-environment checks, and consolidated JSON and Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud QA engineers use this skill to verify Huawei Cloud skills through an eight-phase pipeline that checks installation, extracts capabilities, researches CLI/SDK/API feasibility, generates tests, runs selected live-environment checks, derives orchestration scenarios, and produces final reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run live Huawei Cloud tests and may create, update, or delete cloud resources when write execution is enabled.

Mitigation: Use an isolated test account or project, keep ALLOW_WRITES and ALLOW_REAL_E2E unset until generated cases are reviewed, and confirm cleanup instructions after execution.

Risk: The skill requires Huawei Cloud credentials for live phases.

Mitigation: Use least-privilege, short-lived credentials configured out-of-band through environment variables or an existing hcloud profile; do not paste AK/SK values into chat or commands.

Risk: Sibling skill auto-scan can expand orchestration coverage beyond the explicitly named skill.

Mitigation: Run with --no-siblings unless cross-skill testing is intended, or use --sibling-limit to bound the scope.

Risk: Test artifacts and reports are retained in <skill-name>-test-files and may contain operational details.

Mitigation: Periodically inspect, archive, or delete retained test files according to the environment's data-retention policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-tester)
- [Huawei Cloud hcloud CLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)
- [Architecture](references/architecture.md)
- [Output Schema Specification](references/output-schema-spec.md)
- [Phase Details](references/phase-details.md)
- [Phase Transition Rules](references/phase-transition-rules.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Agent Protocol](references/agent-protocol.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured JSON phase summaries, final JSON report, Markdown report, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written under a sibling <skill-name>-test-files directory and include phase-N-summary.json files plus report/test-report.json and report/test-report.md.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
