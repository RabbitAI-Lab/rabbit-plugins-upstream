## Description: <br>
Generates bidding-competition intelligence reports for a named company, including business focus, winning strength, key customers, competitor overlap, public-risk notes, and optional side-by-side company comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, bidding teams, and analysts use this skill to research a competitor or supplier from public bidding data and produce a traceable Markdown report plus a shareable HTML report. It supports single-company due diligence, two-company comparisons, and lightweight follow-up monitoring prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-register a vendor account using device features and persist an API key under the user's home directory. <br>
Mitigation: Prefer manually setting ZLBX_API_KEY; if no key is configured, proceed with auto-registration only after explicit user consent. <br>
Risk: The workflow uses paid API calls and optional contact lookups can add cost. <br>
Mitigation: Tell the user the expected credit budget before analysis and pause for approval before exceeding the documented budget. <br>
Risk: Generated reports may include signed platform links or contact data that provide access to vendor-hosted information. <br>
Mitigation: Review generated reports before forwarding them and share only when signed links and any contact data are appropriate for the audience. <br>
Risk: Competitive intelligence about real companies can be misleading if unsupported or phrased as a definitive allegation. <br>
Mitigation: Use traceable source data, state data gaps, keep public-risk notes factual, and avoid unsupported or defamatory conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/competitor-intel-analysis) <br>
- [Workflow guide](references/workflow.md) <br>
- [API quick reference](references/api-quick.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration flow](references/auto-register.md) <br>
- [ZhiLiao bidding intelligence platform](https://agent.zhiliaobiaoxun.com) <br>
- [Manual registration and billing portal](https://ai.zhiliaobiaoxun.com/?ch=s118) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with optional self-contained HTML report file and absolute file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ZLBX_API_KEY or a local ~/.zlbx/config.json credential; paid API calls are budgeted before analysis; contact data and signed platform links may appear in reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
