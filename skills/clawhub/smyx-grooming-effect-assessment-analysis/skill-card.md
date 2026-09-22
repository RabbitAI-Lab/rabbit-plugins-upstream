## Description:

AI-powered pet grooming effect assessment: detects mat residue area, dandruff coverage, and coat smoothness from post-grooming images, outputs a 0-100 grooming score with targeted re-grooming suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care service providers use this skill to evaluate post-grooming pet images or videos for mat residue, dandruff coverage, coat smoothness, and whether additional grooming is suggested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, media URLs, report history, and an internally generated identity may be sent to publisher-operated services.

Mitigation: Use only with media and report data appropriate for the publisher service, and disclose or review that remote processing path before use.

Risk: Default configuration includes plaintext development endpoints and local SQLite storage for reusable tokens.

Mitigation: Review or fix endpoint configuration before normal use, prefer trusted HTTPS production endpoints, and restrict or clear local token storage as appropriate.

Risk: The skill provides visual grooming-effect assessment, not veterinary diagnosis or treatment advice.

Mitigation: Treat scores and re-grooming suggestions as grooming guidance only, and use qualified care channels for suspected health issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with score, findings, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-selected file path.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
