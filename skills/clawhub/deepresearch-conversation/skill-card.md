## Description: <br>
Qianfan DeepResearch uses the Baidu Qianfan DeepResearch Agent API to generate structured long-form research reports and return Markdown and HTML download links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ide-rea](https://clawhub.ai/user/ide-rea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run Baidu Qianfan DeepResearch for industry research, market analysis, competitor analysis, technical surveys, policy interpretation, and decision-support reports when a structured long report is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics and generated report content are sent to Baidu Qianfan under the user's API key. <br>
Mitigation: Install and run the skill only when that data sharing is acceptable for the intended use case. <br>
Risk: API keys may be exposed if pasted into chat transcripts or shell history. <br>
Mitigation: Prefer QIANFAN_API_KEY or another secure secret mechanism instead of passing keys directly in conversation or command lines. <br>
Risk: The workflow automatically skips provider clarification and confirms the generated outline. <br>
Mitigation: Review the research query before running so the provider receives a precise topic and scope. <br>


## Reference(s): <br>
- [DeepResearch API documentation](references/api.md) <br>
- [DeepResearch workflow documentation](references/workflow.md) <br>
- [ClawHub release page](https://clawhub.ai/ide-rea/skills/deepresearch-conversation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-facing response with a JSON-producing command-line workflow and Markdown/HTML report download links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Baidu Qianfan API key and may run for 10-30 minutes while the provider generates the report.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
