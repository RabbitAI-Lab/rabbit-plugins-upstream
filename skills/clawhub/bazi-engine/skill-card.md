## Description:

bazi-engine is a Four Pillars (BaZi) astrology skill that collects birth details, computes a deterministic chart and luck cycles, and returns traceable traditional interpretations with classical-source citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruanxiaoer888](https://clawhub.ai/user/ruanxiaoer888)

### License/Terms of Use:

MIT for code; CC BY-NC-SA 4.0 for data

## Use Case:

External users use this skill to generate BaZi chart reports, annual/monthly/daily fortune readings, compatibility checks, family-role analysis, and element-remediation guidance from supplied birth information. Developers and agents can also use the included offline engine and knowledge base to produce structured Markdown or visual chart reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for personal birth details and may reference face or palm photo analysis.

Mitigation: Use a pseudonym, share only the minimum birth details needed for the requested chart, and avoid providing face or palm photos unless that separate analysis is explicitly intended.

Risk: Fortune-telling output can be mistaken for factual health, lifespan, financial, legal, or relationship advice.

Mitigation: Present readings as cultural or entertainment content and direct users to qualified professionals for medical, financial, legal, or major relationship decisions.

Risk: The monitoring utility can use a GitHub token and a local fingerprint file.

Mitigation: Do not run tools/monitor_usage.js unless publisher-side monitoring is intended and the operator has reviewed the token and local-file behavior.

Risk: The artifact contains a dual-license model with non-commercial share-alike terms for data.

Mitigation: Confirm whether the intended deployment uses code, data, or both, and review the data-license terms before commercial reuse of the knowledge base or verdict library.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruanxiaoer888/skills/bazi-engine)
- [README.en.md](README.en.md)
- [SKILL.md](SKILL.md)
- [Knowledge base README](kb/README.md)
- [Data license](LICENSE-DATA)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown reports with tables and optional offline HTML/SVG chart outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses birth date, birth time, gender, birthplace, and optional counterpart birth details for compatibility analysis.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
