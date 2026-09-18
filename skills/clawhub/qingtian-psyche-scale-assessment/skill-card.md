## Description:

Chinese-language mental-health self-assessment skill for administering common self-report scales, scoring responses, assigning bands, and generating local HTML reports with crisis-intervention guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangdaozhenren](https://clawhub.ai/user/wangdaozhenren)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run Chinese-language self-report screening scales for mood, anxiety, stress, sleep, mindfulness, self-esteem, burnout, attachment, and related domains, then summarize scores and generate a local report. Results are informational only and must not be treated as diagnosis, medication advice, therapy, or a substitute for professional assessment.

### Deployment Geography for Use:

Global, with Chinese-language content and China-oriented crisis resources.

## Known Risks and Mitigations:

Risk: Suicide-risk or death-related answers may not always trigger the promised crisis help.

Mitigation: Before deployment, review all depression and broad symptom scales, add crisis triggers for every self-harm, suicide, or death-related item, and keep crisis resources before score presentation.

Risk: Sensitive mental-health reports may be saved locally.

Mitigation: Make local report saving opt-in or clearly confirmed, and tell users to remove personally identifying details before generating reports.

Risk: Authorization requirements vary across the bundled psychological scales, especially for commercial use.

Mitigation: Verify each scale against the source and licensing notes before release, and obtain required publisher permissions where the scale requires authorization.

## Reference(s):

- [Skill README](README.md)
- [Safety Protocol](references/safety_protocol.md)
- [Scale Authority and Licensing Notes](references/scale_authority.md)
- [Sample Report](examples/sample_report.md)
- [ClawHub Skill Page](https://clawhub.ai/wangdaozhenren/skills/qingtian-psyche-scale-assessment)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Chinese conversational text, Markdown summaries, JSON-backed scoring data, and self-contained HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be saved locally under reports/; crisis resources should appear before scores when triggered.]

## Skill Version(s):

0.1.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
