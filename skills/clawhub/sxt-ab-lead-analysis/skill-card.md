## Description: <br>
私信通(私信AI) AB 实验留资效果分析全流程 playbook, 用于从线上埋点 CSV 重建会话、标注留资信号、比较实验组与对照组、处理行业 mix、进行漏斗分层和 OR 归因, 并形成在线报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zh-i9](https://clawhub.ai/user/zh-i9) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Analysts, data scientists, and operators use this skill to evaluate private-message AI AB experiments for lead conversion, including session reconstruction, lead-signal definitions, confidence intervals, industry standardization, merchant pairing, funnel analysis, and OR attribution. It can also guide similar binary-outcome conversation analyses such as deal conversion or contact-addition rates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles private-message logs and contact-lead data, and the rubric pipeline can send sampled conversation text to a remote LLM service. <br>
Mitigation: Use only when authorized to process the data and call that service; redact or pseudonymize identifiers and contact details before analysis. <br>
Risk: Generated reports and intermediate outputs may contain sensitive conversation-derived findings. <br>
Mitigation: Keep outputs in a controlled directory, review results before sharing, and confirm intentionally before updating an online report with force-style update options. <br>


## Reference(s): <br>
- [Data Schema and Lead Definitions](references/data-schema.md) <br>
- [LLM Rubrics to OR Attribution Pipeline](references/or-pipeline.md) <br>
- [Rubric Library](references/rubrics_final.json) <br>
- [OR/FDR Calculation Script](scripts/or_fdr.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON/JSONL data conventions and Python script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided CSV logs and, for the rubric judging pipeline, authorized access to the named remote LLM service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
