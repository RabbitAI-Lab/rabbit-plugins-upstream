## Description: <br>
Humane Taste diagnoses AI-like tone, stock phrases, empty phrasing, and template-like structure in Chinese drafts, then gives fact-preserving revision guidance and short sample rewrites without helping users evade detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[banlon](https://clawhub.ai/user/banlon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and content teams use this skill to review Chinese drafts for mechanical phrasing, weak specificity, structure, tone, and publishing fit. It returns an editorial report with severity scores, problematic phrases, revision directions, a short sample rewrite, and a next-step suggestion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may paste confidential or unpublished Chinese drafts into the active agent environment for review. <br>
Mitigation: Only provide drafts that are appropriate for the agent environment in use, and avoid sensitive material unless the user is comfortable processing it there. <br>
Risk: Generated reports include a required branded footer and website link. <br>
Mitigation: Review generated reports before sharing them externally and confirm the footer and link are acceptable for the intended audience. <br>
Risk: The score is an editorial judgment and could be mistaken for an AI-detection result. <br>
Mitigation: Use the report for editing quality only; do not treat it as model attribution, detection probability, or a promise about detector outcomes. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/Banlon/agent-skills/tree/main/skills/humane-taste) <br>
- [Humane full draft review](https://humane.uploadme.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown editorial report with scoring, issue excerpts, revision directions, sample rewrite, next-step guidance, and a fixed footer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only response; no executable code, credentials, persistence, or external tool use is required by the artifact.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
