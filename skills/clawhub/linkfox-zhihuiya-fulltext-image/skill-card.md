## Description: <br>
Retrieves full-text patent images, including drawings, figures, diagrams, and charts, from the Zhihuiya patent data service by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent analysts, IP teams, and agent users use this skill to retrieve and present visual content from a specific patent document. It is intended for patent-image lookup by patent ID or publication number, not broader patent search or legal-status analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers and session or app metadata are sent to LinkFox's gateway. <br>
Mitigation: Review confidentiality before use and avoid running the skill on sensitive patent searches unless the user accepts that data transfer. <br>
Risk: Requests consume paid LinkFox credits, with the artifact documenting an 81-credit cost. <br>
Mitigation: Tell the user about cost before repeated or follow-up retrievals and avoid automatic retries or pagination without confirmation. <br>
Risk: Full API responses and cache files are stored locally under a LinkFox output directory. <br>
Mitigation: Treat saved response files as potentially sensitive and remove or protect them according to the user's data-handling needs. <br>
Risk: The skill directs agents to submit feedback text to a separate LinkFox endpoint. <br>
Mitigation: Do not include confidential user content in feedback and seek explicit user permission when feedback could reveal sensitive context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-fulltext-image) <br>
- [智慧芽-全文附图 API 参考](references/api.md) <br>
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown summaries and tables, JSON API responses, and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a patent ID or publication number; each request returns up to 100 images and may consume paid credits.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
