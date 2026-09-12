## Description:

Manages and analyzes Huawei Cloud CTS audit data through the hcloud CLI, including tracker lifecycle, trace queries, operation and notification listing, retention checks, and confirmed create/delete workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and security teams use this skill to query Huawei Cloud CTS audit traces, inspect trackers and notifications, analyze retention coverage, and prepare managed changes that require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Huawei Cloud credentials and can access CTS audit data.

Mitigation: Use least-privilege CTS credentials, prefer read-only permissions for query and analysis, and grant create/delete permissions only for approved management workflows.

Risk: Create and delete workflows can change tracker or notification configuration.

Mitigation: Preview the exact hcloud command and expected effect, verify OBS bucket or SMN prerequisites, and execute only after explicit user confirmation.

Risk: Bundled quality reporting can send cloud-authenticated telemetry to a configurable endpoint.

Mitigation: Disable quality reporting unless explicitly approved, avoid custom reporting endpoints, and do not set SKILL_QUALITY_INSECURE.

Risk: The hcloud installer URL points to a downloadable binary archive.

Mitigation: Install hcloud from an official pinned release or verify the archive with an approved checksum before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cts-trace-management)
- [hcloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM policies](references/iam-policies.md)
- [CLI installation guide](references/cli-installation-guide.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Test report](references/test-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with hcloud command examples, structured result summaries, and JSON-oriented outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query and analysis actions may run automatically; create and delete actions require preview and explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
