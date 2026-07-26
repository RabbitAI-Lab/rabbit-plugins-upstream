## Description: <br>
Determines nine TCM constitution types including Yin deficiency, Yang deficiency, Qi deficiency, phlegm-dampness, and blood stasis through facial features and physical signs, and provides personalized health preservation and conditioning suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit face photos, videos, or media URLs for Traditional Chinese Medicine constitution analysis and to retrieve prior report records. It returns structured constitution categories, scores, health-risk notes, and wellness suggestions for reference, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images, videos, and health-related analysis data are sent to cloud services. <br>
Mitigation: Use only with informed consent, avoid sensitive or private signed URLs, and confirm retention, deletion, and processing terms before deployment. <br>
Risk: The skill can silently create or reuse account identity state and retrieve cloud report history. <br>
Mitigation: Run it under an intended workspace identity, isolate test and production workspaces, and review report-history access expectations with users. <br>
Risk: Service tokens and account state may be stored locally in the workspace. <br>
Mitigation: Restrict workspace file access, avoid sharing the workspace with untrusted users, and remove or rotate tokens when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON text, with an optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output detail can be selected as basic, standard, or json; history queries return structured report lists from the cloud API.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
