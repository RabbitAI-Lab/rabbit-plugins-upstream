## Description: <br>
Activate when a KPI is improving without the underlying outcome improving, people may be gaming a metric, rewards are being tied to a number, an algorithm is producing unintended results, or a test or audit system is being designed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and business operators use this skill to stress-test metrics, incentives, audits, rankings, benchmarks, and algorithmic optimization systems for Goodhart-style failure modes. It helps identify gaming vectors, classify the failure mechanism, and design multi-metric, audit, rotation, and independent goal-measurement countermeasures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may apply the Goodhart frame to descriptive metrics with no proxy gap or stakes attached. <br>
Mitigation: Use the skill's fit checks and Not when guidance before running the process. <br>
Risk: The skill can produce plausible governance recommendations that still need domain validation. <br>
Mitigation: Review the proposed metric design, audit schedule, drift threshold, and owner before using it in a high-stakes system. <br>
Risk: Source quality matters for historical and AI-benchmark examples. <br>
Mitigation: Review the linked primary sources and examples when evidence quality affects the decision. <br>


## Reference(s): <br>
- [Sources - goodharts-law](references/sources.md) <br>
- [Goodhart 1975 (M3) and Strathern 1997 (RAE)](examples/goodhart-1975-m3-and-strathern-1997-rae.md) <br>
- [AI benchmarks and engagement metrics as targets (2023-2026)](examples/ai-benchmark-and-engagement-gaming-2023-2026.md) <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/goodharts-law) <br>
- [deciqAI Goodhart's Law page](https://www.deciqai.com/c/goodharts-law) <br>
- [Machine-readable skill metadata](https://www.deciqai.com/s/goodharts-law.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown with structured fields and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a Goodhart-robust design summary with metric, underlying goal, gaming vectors, mechanism category, countermeasures, audit plan, drift threshold, retirement criteria, and owner.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
