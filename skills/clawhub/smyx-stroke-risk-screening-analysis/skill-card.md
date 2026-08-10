## Description: <br>
Combines TCM facial feature recognition with physiological indicator information to provide early warnings of high-risk stroke conditions such as cerebral infarction and cerebral hemorrhage, and provides lifestyle intervention suggestions and medical guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze face images or videos, optionally with physiological indicators, for stroke-risk screening reports, lifestyle intervention suggestions, medical guidance, and cloud report-history lookup. The generated health guidance is screening support and does not replace professional medical examination or diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive face images or videos, health indicators, and report-history requests through configured Life Emergence cloud services. <br>
Mitigation: Use it only after confirming the provider's privacy, retention, deletion, and account-linking practices, and obtain appropriate user consent before sending real medical data. <br>
Risk: The skill may create or reuse a persistent local identity and tokens for account-linked report access. <br>
Mitigation: Review identity and token storage before installation, remove stale credentials when no longer needed, and prefer explicit confirmation before retrieving historical reports. <br>
Risk: Stroke-risk screening output could be mistaken for a medical diagnosis. <br>
Mitigation: Present results as screening guidance only and direct users to professional medical examination or urgent care when high-risk signs are reported. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown or JSON screening report, with optional saved report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk level, risk score, facial-feature observations, health warnings, lifestyle suggestions, medical guidance, report links, and report-history tables.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
