## Description:

VMware Harden helps agents run VMware cyber compliance audits, baseline checks, drift detection, remediation suggestions, and dashboard or report workflows for vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and VMware platform operators use this skill to scan vSphere, ESXi, and NSX estates against supported compliance baselines, inspect coverage and drift, and collect remediation advice. The skill is intended for point-in-time compliance assessment and agent-assisted reporting, with infrastructure changes requiring explicit approval through the appropriate remediation path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill under-discloses a remediation path that can initiate real infrastructure changes through other skills.

Mitigation: Require explicit approval, audit review, and environment scoping before enabling remediation extras, using vmware-harden apply, or dispatching changes through a pilot workflow.

Risk: Compliance evidence may be sent to Anthropic when live remediation advice is enabled.

Mitigation: Avoid sending compliance evidence to Anthropic unless policy permits it, or run without ANTHROPIC_API_KEY so the advisor uses local fallback suggestions.

Risk: The web dashboard can expose compliance posture data if it is made reachable beyond the local host.

Mitigation: Keep the dashboard bound to localhost or place it behind appropriate access controls.

Risk: Server-resolved GitHub import provenance is unavailable for this release.

Mitigation: Prefer verified package provenance before production deployment and review the release evidence before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Clawdis Homepage](https://github.com/vmware-skills/VMware-Harden)
- [Capabilities Reference](artifact/references/capabilities.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [STIG Content Sync](artifact/references/stig-content-sync.md)
- [Cross-Skill Workflows](artifact/references/cross-skill-workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and JSON or report summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses should preserve coverage and truncation fields and distinguish remediation suggestions from executed changes.]

## Skill Version(s):

1.10.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
