## Description:

Analyzes fixed-camera elder home video for dazing, sighing, and self-talking indicators, then produces behavior statistics, emotional-risk prompts, and report or history outputs for caregivers and community workers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, community workers, and care-platform operators use this skill to process solo-living elder camera footage, summarize observed behavior indicators, and retrieve cloud-hosted emotional-risk reports. It provides behavior-based risk prompts and recommendations, not medical diagnosis or psychological scale scoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home-camera footage, optional audio, derived behavior reports, and identity-linked metadata may be sent to provider cloud services.

Mitigation: Use the skill only with informed consent from the monitored person or authorized representative, confirm the provider's data handling terms, and avoid uploading content that is not necessary for the care workflow.

Risk: Bedroom or audio monitoring can expose especially sensitive private information.

Mitigation: Prefer non-bedroom camera placement, minimize audio use, and consider privacy-preserving modes such as body outline or face masking when available.

Risk: Local identity records, stored tokens, and cloud history retrieval can associate reports with a specific person over time.

Mitigation: Review how identities, tokens, and report histories are stored, separated by user, rotated, and deleted before deployment.

Risk: Behavior indicators may be mistaken for clinical conclusions.

Mitigation: Treat outputs as care prompts based on observed behavior only; route diagnosis, psychological scoring, and treatment decisions to qualified professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown summaries and tables, JSON analysis results, report links, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are behavior-based observations and care prompts; they are not clinical diagnoses, PHQ-9 or GDS-15 scores, prescriptions, or treatment plans.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
