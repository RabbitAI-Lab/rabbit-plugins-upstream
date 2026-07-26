## Description: <br>
Conducts intelligent video search based on target and semantic descriptions; supports conventional target retrieval, natural language description retrieval, and vectorized model matching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to search video content for specified objects, people, actions, or natural-language descriptions and return structured analysis or historical report results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos or video URLs may be sent to lifeemergence.com services for analysis. <br>
Mitigation: Use only media and URLs whose external service processing is acceptable for the deployment context. <br>
Risk: The skill can silently create or reuse an internal identity, store tokens locally, and fetch cloud history reports under that identity. <br>
Mitigation: Install only for trusted publishers and review identity, token storage, and cloud-history behavior before deployment. <br>
Risk: The scanner verdict is suspicious even though no specific risk findings were listed. <br>
Mitigation: Review the skill and its network/data flows before installation, especially for sensitive local media or private/internal URLs. <br>


## Reference(s): <br>
- [API 接口文档](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-video-search-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown or JSON analysis results, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report links and historical report tables when requested.] <br>

## Skill Version(s): <br>
999.999.999 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
