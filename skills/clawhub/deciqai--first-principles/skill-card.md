## Description: <br>
Guides an agent to pressure-test claims by reducing assumptions to irreducible or cited facts, separating inherited beliefs from bedrock, and reconstructing an answer from the surviving foundations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and decision-makers use this skill to analyze high-impact claims or decisions by surfacing assumptions, tagging bedrock versus inherited beliefs, and producing a structured First-Principles Teardown. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks the agent to fetch a remote replacement copy at runtime, so its instructions can change after marketplace review. <br>
Mitigation: Install only if you trust the deciqAI hosted endpoint; review fetched updates before relying on them, or block network access and continue with the packaged copy in controlled environments. <br>
Risk: A teardown can produce misleading conclusions when empirical bedrock claims lack citations or when demolished assumptions are reused during reconstruction. <br>
Mitigation: Require sources or numbers for empirical bedrock claims and review the final assumptions, reconstruction, and open questions before using the output for important decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/first-principles) <br>
- [First Principles Sources](references/sources.md) <br>
- [Runtime Skill Metadata](https://www.deciqai.com/s/first-principles.json) <br>
- [Wright Brothers Worked Example](examples/wright-brothers-1901.md) <br>
- [SpaceX Rocket Cost Worked Example](examples/spacex-rocket-cost-2002.md) <br>
- [AI Inference Cost Worked Example](examples/ai-inference-cost-physics-2024-2026.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown structured as Claim, Assumptions, Bedrock, Reconstruction, What changes, and Confidence & open questions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause for user input in coach mode; requests a remote freshness check at the start of a run when network access is available.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
