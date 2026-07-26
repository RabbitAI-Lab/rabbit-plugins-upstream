## Description: <br>
Fxbaogao Deep Research helps agents conduct structured research on industries, companies, or topics by decomposing questions, searching fxbaogao reports, checking key facts against PDFs, and producing traceable Markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quickzhang](https://clawhub.ai/user/quickzhang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and developers use this skill to turn fxbaogao report searches into structured research workspaces, single-report close reads, fact cards, comparison frameworks, and final Markdown research reports with source links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an fxbaogao API key and sends report-search topics, report IDs, and related queries to the fxbaogao API. <br>
Mitigation: Confirm the user is comfortable sharing those queries with fxbaogao and provide the API key through the FXBAOGAO_API_KEY environment variable only when needed. <br>
Risk: Paragraph API summaries may be insufficient for formal conclusions, quotations, key figures, or page-level evidence. <br>
Mitigation: For formal research, original quotes, key data, charts, or uncertain claims, download the PDF and verify facts against the PDF text, page numbers, or figure labels. <br>
Risk: Research conclusions may overstate certainty if report assumptions, data scopes, or source disagreements are not tracked. <br>
Mitigation: Record report IDs, official reading links, source scope, confidence, disagreements, risks, uncertainties, and next verification steps in the Markdown workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/quickzhang/skills/fxbaogao-deep-research) <br>
- [fxbaogao API usage](references/api-usage.md) <br>
- [Research playbook](references/research-playbook.md) <br>
- [Report reader playbook](references/report-reader-playbook.md) <br>
- [fxbaogao API](https://api.fxbaogao.com) <br>
- [fxbaogao report reader](https://www.fxbaogao.com/view?id=<reportId>) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, research workspace files, API request examples, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs preserve report IDs, source links, fact cards, evidence chains, risks, uncertainties, and next-step recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
