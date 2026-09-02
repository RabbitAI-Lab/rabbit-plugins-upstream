## Description:

Medical Device Cybersecurity（医疗器械网络安全） helps agents provide medical device cybersecurity compliance guidance, checklists, SBOM templates, vulnerability triage guidance, and regional requirement summaries for FDA, EU, and China NMPA workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Regulatory, R&D, product security, and information security teams use this skill to reason about medical device cybersecurity obligations, prepare submission-oriented checklists, draft SBOM field structures, and plan vulnerability management activities. It is useful for agents supporting compliance planning across FDA, EU, and China NMPA contexts.

### Deployment Geography for Use:

Global, with specific reference coverage for the United States, European Union, and China.

## Known Risks and Mitigations:

Risk: Regulatory guidance may become outdated after the package reference date.

Mitigation: Verify current FDA, EU, and NMPA requirements before using outputs for real submissions or quality-system decisions.

Risk: The bundled security audit report contains mismatched file and tool names.

Mitigation: Treat the server security verdict as authoritative for this release and correct the audit-report naming mismatch before relying on it as a precise audit record.

Risk: The vulnerability triage command uses local keyword rules and CVSS-style labels rather than a formal CVSS calculation.

Mitigation: Use the command for initial triage only, then confirm severity with a formal CVSS vector and product-specific risk assessment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/medical-device-cybersecurity)
- [01 网络安全全景与监管](references/01-网络安全全景与监管.md)
- [02 美国 FDA 网络安全要求](references/02-美国FDA网络安全要求.md)
- [03 欧盟网络安全要求](references/03-欧盟网络安全要求.md)
- [04 中国 NMPA 网络安全要求](references/04-中国NMPA网络安全要求.md)
- [05 SBOM 实操](references/05-SBOM实操.md)
- [06 漏洞管理与协调披露](references/06-漏洞管理与协调披露.md)
- [07 网络安全体系与文档](references/07-网络安全体系与文档.md)
- [08 FAQ](references/08-FAQ.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown prose, command examples, checklists, and JSON SBOM templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled local toolkit uses Python standard library commands and prints results to standard output.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
