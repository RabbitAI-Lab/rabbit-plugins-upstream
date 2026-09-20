## Description:

Qingtian Free Psych Resources helps an agent find and present free mental health support resources, AI companionship options, and self-assessment workflows across multiple languages, with crisis signals prioritized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support agents use this skill to locate free counseling, listening, crisis, AI companionship, and self-assessment resources by region, language, service type, and availability. The skill is informational and should route crisis signals to human emergency or hotline resources before ordinary recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Assessment output may be unsafe for urgent decisions if high-risk questionnaire items are not connected to crisis handling.

Mitigation: Treat assessments as informational only and do not rely on SDS, CES-D, SCL-90, or FFMQ outputs for urgent safety decisions until crisis metadata and scoring keys are reviewed and corrected.

Risk: Crisis resource recommendations can be wrong if the user's location is assumed.

Mitigation: Confirm the user's location before relying on crisis resources and prioritize local emergency services or human crisis lines.

Risk: Generated assessment reports may contain sensitive mental health information and may be saved locally.

Mitigation: Avoid saving reports in shared or synced folders unless the user explicitly agrees.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangdaozhenren/skills/qingtian-free-psych-resources)
- [Dynamic resource sheet](https://docs.qq.com/sheet/DTG5OU3Jad1dEeGNt?tab=BB08J2)
- [Resource schema](artifact/references/schema.md)
- [China resources baseline](artifact/references/china-resources.md)
- [International resources baseline](artifact/references/international-resources.md)
- [Online platforms baseline](artifact/references/online-platforms.md)
- [AI tools baseline](artifact/references/ai-tools.md)
- [Source directories and verification priority](artifact/references/source-directories.md)
- [Assessment safety protocol](artifact/modules/psyche-scale-assessment/references/safety_protocol.md)
- [Scale authority and licensing notes](artifact/modules/psyche-scale-assessment/references/scale_authority.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown resource cards, multilingual guidance, and optional local HTML assessment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source and verification status for resources; assessment reports may contain sensitive user-provided mental health data.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata, released 2026-09-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
