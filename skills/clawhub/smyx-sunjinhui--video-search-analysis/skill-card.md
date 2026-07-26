## Description: <br>
Searches videos for objects, people, or natural-language descriptions and returns structured retrieval results with report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to locate target footage in videos using object, person, keyword, or semantic descriptions. It can also retrieve cloud-hosted historical video search reports for the current skill identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos, video URLs, and report history may be sent to a third-party cloud service. <br>
Mitigation: Install only after reviewing endpoint ownership, retention expectations, and whether cloud processing is acceptable for the intended video data. <br>
Risk: The skill may silently create or reuse an identity and store service tokens in a local workspace database. <br>
Mitigation: Run it in an isolated workspace when evaluating, inspect local data storage, and remove stored credentials or identities when no longer needed. <br>
Risk: Video search results and generated reports may be incomplete or incorrect. <br>
Mitigation: Treat returned matches and report links as assistive analysis and verify important findings against the source video. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/video-search-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON text, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns structured analysis content, report links, and historical report listings when requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
