## Description:

Through a fixed camera in the reptile enclosure, the system captures a high-definition image (or a static video frame) once excrement is found, and uses AI visual analysis to identify urate (white/milky-white crystals or paste, common in lizards, geckos, etc.) - including its size (pixel area) - and to identify the morphology of feces (normally formed log, soft pasty, watery, or bloody).

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, farms, and app developers use this skill to analyze enclosure images or video frames of reptile excrement before cleaning. It produces visual assessment reports for urate size/color and feces morphology, flags unreliable imagery, and suggests observation or veterinary follow-up without providing diagnoses or prescriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media and history queries are handled through cloud analysis services and may be associated with an automatically created or reused identity.

Mitigation: Use only when cloud analysis and account-linked history are approved for the media; avoid sensitive facility images unless those data flows are acceptable.

Risk: The security evidence reports local token storage, silent identity creation or reuse, and possible workspace API-key file access.

Mitigation: Review identity, token, and credential handling before deployment, and restrict use to environments where those controls are acceptable.

Risk: Visual assessment can be unreliable when images are obstructed, color-shifted, below 1080p, or missing a size reference.

Mitigation: Treat such cases as unreliable and request a clear overhead image with complete urate and feces regions, white lighting, and a known-size reference.

Risk: The skill provides visual health prompts that could be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Keep outputs limited to visual assessment, avoid drug names, dosages, and procedures, and direct significant abnormalities to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-excrement-analysis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Reptile excrement analysis API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown-style report text with structured JSON analysis content and optional report export link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image/video-frame files, media URLs, and account-linked historical report listing through the skill's command-line workflow.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
