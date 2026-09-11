## Description:

Diagnoses Huawei Cloud CDN domain DNS resolution issues by checking domain access with hcloud, probing A-record resolution with dnspython, and comparing resolved IPs against Huawei Cloud CDN attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, CDN operators, and support engineers use this skill to diagnose why a CDN domain is not resolving to Huawei Cloud CDN, including permission checks, DNS probe results, IP attribution, and remediation guidance. It is intended for read-only diagnosis and not for DNS or CDN configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated hcloud commands could expose or misuse Huawei Cloud credentials if the agent asks for, echoes, or handles AK/SK secrets directly.

Mitigation: Use a least-privilege Huawei Cloud account, rely on configured CLI or environment credentials, and never paste AK/SK values into chat.

Risk: The artifact includes guidance around changing the host system DNS resolver for follow-up probing.

Mitigation: Do not let the skill or agent change the system DNS resolver automatically; require the user to perform any resolver change manually and rerun the read-only probe.

Risk: Unsafe shell-string construction for authenticated CLI calls could run unintended commands or target the wrong domain or region.

Mitigation: Validate the domain and region before running hcloud commands, use the documented --key=value parameter format, and avoid building shell commands through untrusted string concatenation.

Risk: The DNS probe depends on dnspython and may inherit unexpected package behavior if installed globally or from an unreviewed source.

Mitigation: Install dnspython in a dedicated virtual environment with a pinned, reviewed version before running the probe.

## Reference(s):

- [Step 1: Credential Validation and Domain Permission Check](references/task-permission-check.md)
- [Step 2: DNS Resolution Probe](references/task-dns-resolve.md)
- [Step 3: IP Attribution Check](references/task-ip-attribution.md)
- [Step 4: Generate Diagnosis Report](references/task-report-generation.md)
- [Prohibited Operations](references/prohibited-operations.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [API and CLI Command Reference](references/related-apis.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/hcloudcli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Structured text or Markdown diagnosis report with inline shell commands and JSON-derived findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include analysis time, target domain, expected CNAME, resolved IPs, diagnosis item status, conclusion, and remediation suggestions.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
