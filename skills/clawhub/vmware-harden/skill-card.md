## Description:

Guides VMware compliance scans, baseline checks, drift analysis, and remediation advice for vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure and security engineers use this skill to assess VMware environments against built-in or custom compliance baselines, compare scan snapshots, and review proposed remediation steps without directly applying changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Locally stored scan history can expose VMware compliance posture on shared machines or CI runners.

Mitigation: Protect or relocate the local DuckDB and restrict access to its scan artifacts.

Risk: Exposing the web dashboard beyond localhost could disclose compliance findings.

Mitigation: Keep the dashboard on localhost unless access controls are in place.

Risk: Enabling live AI advice can send violation evidence to Anthropic.

Mitigation: Set ANTHROPIC_API_KEY only if that data transfer is acceptable for the environment.

Risk: Overprivileged collector access could expose more VMware environment data than required.

Mitigation: Use a least-privilege, read-only VMware account for upstream collectors.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Harden)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Capabilities](artifact/references/capabilities.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands; scan reports may be text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include violations, coverage, and scan snapshot details; remediation is advisory.]

## Skill Version(s):

1.13.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
