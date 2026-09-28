## Description:

Analyzes pet grooming video files or URLs through cloud APIs to identify stress behaviors such as struggling, panting, and tail tucking, then returns stress-level grading and report links for grooming, veterinary, and pet-care workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, groomers, veterinary clinics, pet-care teams, and agent developers use this skill to submit grooming-session videos or URLs for behavior observation, stress-level assessment, historical report lookup, and report-link generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grooming videos or video URLs are sent to lifeemergence.com cloud services for analysis and report generation.

Mitigation: Use only footage that is permitted under the user's privacy, consent, customer, clinic, or business data-handling rules; avoid sensitive camera footage unless cloud processing is approved.

Risk: The skill can create or reuse a cloud-linked service identity and persist local tokens for report history.

Mitigation: Run the skill in a controlled workspace, review local token storage before reuse or sharing, and clear workspace data when the linked identity should not persist.

Risk: Historical report lookup can retrieve cloud report history associated with the resolved identity.

Mitigation: Confirm the workspace identity before listing reports and avoid using shared workspaces for customer or clinic footage unless report history access is intended.

Risk: Stress-level output is behavior-observation guidance and may be incomplete or incorrect for animal health decisions.

Mitigation: Treat results as observational support, review the underlying video and report before acting, and escalate health or welfare concerns to qualified veterinary or animal-care professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Skill usage demo](https://lifeemergence.com/sample.html)
- [Pet grooming stress analysis API reference](references/api_doc.md)
- [Common AI analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with command examples, analysis summaries, stress-level results, historical report records, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or network video URLs; supports pet type, detail level, output file, and historical report listing options.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
