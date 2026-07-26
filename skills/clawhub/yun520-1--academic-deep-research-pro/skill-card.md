## Description: <br>
Academic Deep Research Pro guides an agent through transparent, multi-cycle web research with user checkpoints, evidence hierarchy, APA 7th citations, and narrative report synthesis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, analysts, and developers use this skill when they need an agent to plan and execute rigorous multi-source research, then produce a reproducible academic-style narrative report with citations and documented uncertainty. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics and source URLs may be exposed through external search and fetch activity during approved research runs. <br>
Mitigation: Use the skill only for topics approved for external web research, review the proposed research plan before approval, and avoid entering confidential subjects or sensitive source material. <br>
Risk: Long-running multi-step research may generate many web requests after the plan is approved. <br>
Mitigation: Approve only bounded research scopes and require the agent to document gaps, failed fetches, and confidence levels in the final report. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yun520-1/skills/academic-deep-research-pro) <br>
- [Research Protocol](artifact/reference/protocol.md) <br>
- [Writing Style Requirements](artifact/reference/writing-style.md) <br>
- [APA 7th Citations](artifact/reference/citations-apa.md) <br>
- [Final Report Template](artifact/reference/report-template.md) <br>
- [Evidence and Quality Standards](artifact/reference/quality-standards.md) <br>
- [Error Handling](artifact/reference/error-handling.md) <br>
- [Parallel Research with sessions_spawn](artifact/reference/parallel-research.md) <br>
- [Deep Research Quick Reference](artifact/quickref.md) <br>
- [Deep Research Example Workflow](artifact/example.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown narrative research reports with APA 7th citations, confidence annotations, limitations, and reference lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow asks for clarification, waits for plan approval before research execution, and requires analysis between web research tool calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
