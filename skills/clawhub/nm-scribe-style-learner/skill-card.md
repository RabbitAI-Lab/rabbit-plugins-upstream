## Description: <br>
Extracts writing style patterns from exemplar text into a reusable profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and content teams use this skill to analyze exemplar writing and create reusable style profiles. The profiles combine quantitative metrics, selected passages, anti-patterns, and validation notes for consistent generation or editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers such as style, voice, and tone may activate the skill more often than intended. <br>
Mitigation: Confirm that style learning is intended before collecting exemplars or generating a profile. <br>
Risk: User-provided exemplar text may contain sensitive, proprietary, or personal writing. <br>
Mitigation: Use only exemplar material that is approved for style reference and remove unnecessary secrets or confidential details. <br>
Risk: A generated profile may overfit limited exemplars or misrepresent the target voice. <br>
Mitigation: Validate the profile against new content, compare metrics to the exemplars, and revise before relying on it for production writing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-style-learner) <br>
- [Scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Feature Extraction Module](modules/feature-extraction.md) <br>
- [Exemplar Reference Module](modules/exemplar-reference.md) <br>
- [Style Application Module](modules/style-application.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with YAML-style profile sections and exemplar passages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include quantitative style metrics, selected exemplars, anti-patterns, and validation notes.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
