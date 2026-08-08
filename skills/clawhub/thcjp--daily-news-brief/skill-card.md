## Description: <br>
Daily News Brief helps an agent collect, summarize, and publish daily briefings on international affairs, economic conditions, and technology developments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and automation teams can use this skill to create recurring news briefings from current-event, economic, and technology inputs. It is not suitable for decisions that require fully deterministic or independently verified facts without human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill advertises broad command execution, file handling, agent orchestration, and external publishing authority. <br>
Mitigation: Require explicit approval for command execution and publishing, restrict allowed sources and commands, and review a preview before any content is posted. <br>
Risk: Generated news briefings may contain stale, incomplete, or misleading claims from external sources or model output. <br>
Mitigation: Require source attribution, check high-impact claims against trusted sources, and keep human review in the publication workflow. <br>
Risk: API credentials or private input data could be exposed during configuration or publishing workflows. <br>
Mitigation: Use scoped credentials, avoid embedding secrets in prompts or files, and review outputs for sensitive data before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-news-brief) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON responses containing news items, summaries, status fields, and metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on live news sources, LLM output, and user-provided API credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
