## Description:

Analyzes household public-area audio/video to detect family conflict signals, wait for a calm window, and suggest neutral aftercare actions such as soft music, gentle voice prompts, app messages, or safety escalation when red-line indicators appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and smart-home developers can use this skill to process living-room, kitchen, or dining-room camera and microphone inputs for conflict event detection, calm-window assessment, aftercare recommendations, and historical report lookup. The skill is intended for household public spaces with consent and is not a substitute for counseling, emergency response, or domestic-safety services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive household audio/video may be processed through cloud services and report history.

Mitigation: Use only with consent from household members, verify backend endpoints, and confirm retention and report-access controls before installation.

Risk: Hidden account and token persistence may affect privacy and access control.

Mitigation: Review identity and token storage behavior before deployment and ensure users can understand and control report association.

Risk: Deployment in private rooms, around minors, or in domestic safety situations can create serious privacy and safety concerns.

Mitigation: Limit use to authorized household public spaces and require stronger controls and clear legal authorization for minors or domestic-safety contexts.

Risk: Aftercare prompts during active or high-risk conflict could worsen a situation.

Mitigation: Require calm-window gating for aftercare and route red-line indicators such as suspected physical violence, dangerous objects, injury signs, or minors present to safety-resource guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-aftercare-suggest-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis with event fields, recommendations, safety resources, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL inputs, history listing, detail-level selection, and optional output-file writing.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact SKILL.md frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
