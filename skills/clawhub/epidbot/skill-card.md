## Description: <br>
Query EpidBot (Brazilian public health data AI assistant) via its REST API. Use when you need epidemiological data analysis, plots, reports, DATASUS queries, plot management, report downloads, code snippets, or dataset uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fccoelho](https://clawhub.ai/user/fccoelho) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and public-health analysts use this skill to query EpidBot via REST for Brazilian epidemiological analysis, generated plots and reports, code snippets, and uploaded dataset management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dataset publishing and update or delete operations can change or remove user content if used without confirmation. <br>
Mitigation: Only run upload, publish, PATCH, DELETE, or bulk-delete actions after explicit user confirmation and after verifying exact dataset, plot, or report IDs. <br>
Risk: Use with sensitive datasets or valuable EpidBot content can expose private information or cause unintended changes. <br>
Mitigation: Review the skill before installing or using it with sensitive datasets, and keep API keys and private dataset contents out of shared outputs. <br>


## Reference(s): <br>
- [EpidBot API base URL](https://epidbot.kwar-ai.com.br) <br>
- [ClawHub skill page](https://clawhub.ai/fccoelho/skills/epidbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown API guidance with JSON examples and HTTP request and response snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EPIDBOT_API_KEY and EPIDBOT_API_URL; chat responses are asynchronous and may include server-hosted image references.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
