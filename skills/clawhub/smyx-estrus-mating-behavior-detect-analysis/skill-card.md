## Description: <br>
Detects estrus behavior in female livestock from continuous barn videos, including mounting acceptance, standing reflex, restlessness, appetite drop, and vulva changes, and outputs an estrus recognition result with an optimal mating time window. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External livestock producers, farm operators, and developers use this skill to submit barn images, videos, or media URLs for estrus behavior analysis, stage classification, mating-window output, and report history retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Barn images or videos, remote media URLs, identity values, and report history are sent to configured external services. <br>
Mitigation: Use only with media and report data approved for those services; avoid sensitive farm footage unless the publisher documents identity handling, retention, and deletion controls. <br>
Risk: The skill can generate or reuse an identity and store user records and auth tokens in the workspace data directory. <br>
Mitigation: Run it in a dedicated workspace with restricted access, and clear the workspace data directory when local identity or token persistence is not desired. <br>
Risk: Estrus stage and mating-window outputs are decision-support signals and may be affected by video quality, occlusion, lighting, or model/API errors. <br>
Mitigation: Treat results as reference material and confirm breeding decisions against farm procedures and qualified reproductive management staff. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-estrus-mating-behavior-detect-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown or JSON text with optional saved output file and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local media paths or media URLs, polls an external analysis API for completion, and can list historical reports for the resolved identity.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
