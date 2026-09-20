## Description:

The single entry point for the ct-series across the full clinical-development lifecycle: a cloud-assisted clinical trial advisor for methodology, design, compliance, QC, site execution, and specialist sibling-skill routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and clinical-development teams use this skill to ask trial methodology, regulatory, GCP, safety, QC, protocol, and competitive-intelligence questions in chat. It forwards non-vague questions to a configured cloud advisor, can route public-data tasks to sibling ct-series skills, and returns source-traceable guidance for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical-trial questions, attachments, recent conversation context, or private operational details may be sent to configured external Coze services.

Mitigation: Use the skill only for content approved for cloud processing; remove subject data, unpublished protocols, sponsor details, and commercial strategy before asking or attaching files.

Risk: The security evidence reports weak consent and redaction controls around sensitive context and a persistent device identifier.

Mitigation: Review outbound behavior and privacy requirements before installation; avoid use in regulated or confidential workflows unless the deployment owner accepts those controls.

Risk: Sibling-skill installation and execution can add packages and run local code.

Mitigation: Authorize sibling-skill installation only for trusted SkillHub packages, and review the package source and security evidence before allowing execution.

Risk: Clinical or regulatory guidance may be incomplete, outdated, or unsuitable for submission without expert review.

Mitigation: Validate outputs against official clinical, regulatory, and institutional sources before relying on them for trial decisions or submissions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Project Homepage](https://github.com/medstatstar/ct-advisor)
- [English User Guide](README.md)
- [Chinese User Guide](README_zh-CN.md)
- [Execution Workflow](references/steps.md)
- [Sibling Skill Tier Gate](references/tier_gate.md)
- [Advanced Operation Notes](references/ADVANCED.md)
- [Reference Source Sites](references/search-sites.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown chat responses, plain text guidance, inline code or shell commands, and generated local files when sibling skills produce artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual English/Chinese responses follow the user's language; source-traceability and official-verification markers may be included for clinical or regulatory claims.]

## Skill Version(s):

0.9.104 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
