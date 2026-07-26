## Description: <br>
Synthesize invariant principles from three or more sources to identify the core pattern that survives across expressions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leegitw](https://clawhub.ai/user/leegitw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and documentation teams use this skill to synthesize three or more related source texts or extraction outputs into Golden Master candidates with supporting evidence and next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive source material may be processed by the user's configured LLM provider during synthesis. <br>
Mitigation: Use non-sensitive or approved source material unless the provider's data handling is acceptable for the content. <br>
Risk: Golden Master candidates are pattern-analysis outputs, not verified truths. <br>
Mitigation: Review synthesized candidates and supporting evidence before treating them as canonical. <br>
Risk: Drift notes may be returned in output or written locally to requires_review.md depending on runtime behavior. <br>
Mitigation: Clarify expected local file-writing behavior before using the skill with sensitive material. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leegitw/skills/principle-synthesizer) <br>
- [Project homepage from ClawHub metadata](https://github.com/live-neon/skills/tree/main/pbd/principle-synthesizer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON object with synthesis results, evidence, metrics, and next steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include share_text when at least one Golden Master candidate is identified.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
