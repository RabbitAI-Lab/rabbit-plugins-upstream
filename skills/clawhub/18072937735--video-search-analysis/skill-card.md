## Description: <br>
Conducts intelligent video search based on target and semantic descriptions, supporting conventional target retrieval, natural-language retrieval, and vectorized model matching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search video files or video URLs for objects, people, scenes, or natural-language descriptions and receive structured analysis results, report links, or cloud report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos, video URLs, and account-linked analysis requests are sent to the lifeemergence.com service. <br>
Mitigation: Use only with data approved for that external service and confirm retention and processing terms before deployment. <br>
Risk: The skill can silently create or reuse a local identity and store identity/token data in the workspace. <br>
Mitigation: Protect the workspace data directory, review token lifecycle controls, and confirm whether silent identity reuse can be disabled. <br>
Risk: Cloud report history can be fetched for the resolved identity. <br>
Mitigation: Limit use to trusted environments and verify that report history access matches the intended user/account boundary. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/18072937735/skills/video-search-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown or JSON-like structured report text, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include analysis details, cloud report history, and report export links returned by the external service.] <br>

## Skill Version(s): <br>
1.0.99 (source: server release metadata; artifact frontmatter declares 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
