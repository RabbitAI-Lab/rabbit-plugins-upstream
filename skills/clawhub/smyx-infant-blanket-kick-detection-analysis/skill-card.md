## Description:

Analyzes night-time crib images or video to estimate infant blanket coverage, detect kicking or blanket-slip events, and produce visual alert reports without medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers of baby-monitoring workflows can use this skill to review night-time crib media for blanket coverage state, kicking motion, blanket-slip events, alert level, and report links. Results are auxiliary visual monitoring outputs and are not a substitute for adult supervision or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant and home-monitoring videos, URLs, and account-linked reports may be sent to configured cloud services.

Mitigation: Use only with guardian consent, authorized media sources, and publisher-provided retention, deletion, endpoint, and access-control terms.

Risk: The skill can silently create or reuse an internal identity and store tokens locally.

Mitigation: Review token storage and identity behavior before deployment, and run only in environments where local credential handling is acceptable.

Risk: The output is an auxiliary visual alert and may miss events or produce incorrect alerts.

Mitigation: Use results as monitoring support only; keep adult supervision and avoid treating outputs as medical advice or a complete safety system.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blanket coverage percentage, coverage state, kick events, alert level, smart-home hints, historical report tables, and saved output files when requested.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
