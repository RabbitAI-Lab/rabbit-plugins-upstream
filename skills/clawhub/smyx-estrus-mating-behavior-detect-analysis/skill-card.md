## Description:

Detects estrus behavior in female livestock from continuous barn videos, including mounting acceptance, standing reflex, restlessness, appetite drop, and vulva changes, and returns an estrus recognition result with an optimal mating time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External farm operators, livestock reproduction teams, and agent users use this skill to analyze barn video or image inputs for estrus behavior, estrus stage, a mating time window, and report links. It is intended as decision support and does not provide breeding operation instructions or farm management advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends barn images or video to a cloud analysis service, and the footage may include people, location-sensitive farm details, or confidential operations.

Mitigation: Review the footage before use, avoid uploading sensitive material unless authorized, and use the skill only where cloud processing is acceptable.

Risk: The security evidence says the skill silently creates or reuses an account identity and stores service tokens locally in the workspace.

Mitigation: Run the skill in a dedicated workspace or account context, restrict workspace access, and clear local identity or token storage when the analysis context changes.

Risk: The skill can retrieve account-scoped historical reports, which may expose prior analysis results for the current local identity.

Mitigation: Verify the active workspace identity before history lookups and limit execution to the intended user or farm account.

Risk: The output is a reference result for estrus and mating timing, not a replacement for farm procedures or professional reproduction guidance.

Mitigation: Treat results as decision support and confirm breeding decisions with farm policy and qualified reproduction personnel.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-estrus-mating-behavior-detect-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Estrus/Mating Behavior API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown report text with structured analysis content, historical report listings, and report links; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail modes; local media is limited by the skill documentation to supported image/video formats and a 10 MB file size cap.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
