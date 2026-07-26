## Description: <br>
Skill Compliance checks skills before domestic platform upload for Chinese compliance issues including financial terms, disclaimers, security redlines, privacy, and regulatory requirements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this skill locally before upload to scan one or more skill directories for domestic platform compliance issues and receive scores, findings, and recommendations. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The local checker reads files under the target skill directory and can write a report to a user-provided output path. <br>
Mitigation: Run it only on intended skill directories and choose output paths carefully. <br>
Risk: Compliance scans are advisory and may not capture every legal or policy requirement. <br>
Mitigation: Use the findings as a preflight review aid and keep final compliance review with the skill developer or qualified reviewer. <br>
Risk: Keyword and rules-based checks can produce false positives or miss context-sensitive issues. <br>
Mitigation: Review reported findings, rule sources, and recommendations before changing or publishing a skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cqdev-ai/skills/skill-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Guidance, Shell commands] <br>
**Output Format:** [Terminal text, JSON reports, and optional report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally over user-selected skill directories with no network access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and changelog indicate 1.1.0 for package contents) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
