## Description: <br>
Determines nine TCM constitution types including Yin deficiency, Yang deficiency, Qi deficiency, phlegm-dampness, and blood stasis through facial features and physical signs, and provides personalized health preservation and conditioning suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit face photos, videos, or media URLs for TCM constitution analysis and to retrieve prior analysis reports. The generated report is wellness-oriented reference material and should not be treated as a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive face/video media and health-related analysis data. <br>
Mitigation: Use it only with clear consent, and avoid submitting third-party media URLs unless rights and consent are established. <br>
Risk: Report history may be associated with an internal identity, and service tokens may be stored in workspace SQLite data. <br>
Mitigation: Install and run it only in trusted workspaces, and restrict access to local skill data and generated reports. <br>
Risk: TCM constitution outputs can be mistaken for medical diagnosis. <br>
Mitigation: Treat reports as wellness reference material, and seek qualified medical care for symptoms or health decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [JSON or Markdown text returned from command-line execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured constitution scores, health-risk notes, conditioning suggestions, report lists, and export links returned by the service.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
