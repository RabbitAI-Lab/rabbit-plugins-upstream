## Description: <br>
Deconstruct video ad creatives into marketing dimensions using Gemini AI. Extracts hooks, social proof, CTAs, target audience, emotional triggers, urgency tactics, and more. Use when analyzing competitor ads, generating creative briefs, or understanding what makes ads effective. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fortytwode](https://clawhub.ai/user/fortytwode) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Marketing teams, creative strategists, and developers use this skill to analyze video ad content and turn transcripts, text overlays, and scene descriptions into structured marketing insights for competitor analysis and creative briefs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ad-derived transcripts, text overlays, and scene descriptions are sent to Gemini/Vertex AI for analysis. <br>
Mitigation: Install only if provider use is permitted; avoid analyzing confidential or regulated creative material unless organizational policy allows it. <br>
Risk: Google service account credentials are required for Vertex AI access. <br>
Mitigation: Use a dedicated least-privileged service account, protect the credential file, and do not commit credentials to source control. <br>


## Reference(s): <br>
- [Meta Video Ad Deconstructor on ClawHub](https://clawhub.ai/fortytwode/skills/meta-video-ad-deconstructor) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, code, configuration, guidance] <br>
**Output Format:** [Plain-text summaries and structured JSON dictionaries containing marketing dimensions, evidence, context, and salience scores.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Gemini through Vertex AI, accepts extracted video transcript, text timeline, and scene timeline inputs, and supports progress callbacks for longer analyses.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
