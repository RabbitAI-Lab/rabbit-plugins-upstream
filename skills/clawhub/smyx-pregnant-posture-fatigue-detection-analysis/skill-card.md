## Description:

Uses a fixed home camera to detect prolonged standing, bending, and related posture of a pregnant woman, track standing duration and bending frequency, and assess fatigue risk; it sends rest reminders via speaker or app when tiring behavior is found and is for health reference only, not medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to analyze fixed-camera home or care-setting video for pregnancy posture and fatigue indicators, including continuous standing duration, bending frequency, suspected heavy lifting, reminders, and historical report lookup. Outputs are wellness-oriented observations and reminders, not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pregnancy-related home-camera footage or video URLs may be sent to the configured cloud analysis service.

Mitigation: Use only with explicit consent from the person recorded, verify service endpoints and retention policy, and avoid sharing footage that is unnecessary for the fatigue-analysis purpose.

Risk: Reports can be linked to an automatically managed identity and account tokens may be stored or transmitted.

Mitigation: Review identity creation and token handling before deployment, protect any local token storage, and install only where this account-linking behavior is acceptable.

Risk: Posture and bending detection may be unreliable when the video lacks a clear full-body view or has clothing and camera-angle ambiguity.

Mitigation: Require stable fixed-camera footage with the full body visible, treat outputs as wellness reminders, and rely on clinical care for symptoms or medical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis)
- [Pregnant posture fatigue API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with optional report links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a file and may return historical report lists from the configured cloud API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
