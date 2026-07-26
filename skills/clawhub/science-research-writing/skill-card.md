## Description: <br>
Use when researchers need to plan, draft, revise, or audit an empirical research paper from their own materials, including Introduction, Methods, Results, Discussion, Conclusion, Abstract, and Title, with evidence-preserving and target-journal-aware guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yila-ai](https://clawhub.ai/user/yila-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers and authors use this skill to plan, draft, revise, or audit empirical research manuscripts from their own supplied materials while preserving evidence boundaries, claim strength, citations, limitations, and section-specific expectations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect confidential manuscripts, datasets, target papers, and writing materials supplied by the user. <br>
Mitigation: Use only materials the author is permitted to share with the agent and avoid providing confidential or restricted research files unless that use is acceptable. <br>
Risk: Manuscript prose can become misleading if missing evidence, conflicting sources, null findings, claim strength, or citation attachment are not reviewed by the author. <br>
Mitigation: Review generated drafts against the source materials, answer requested author-confirmation questions, and use the included draft-invariant checks when local source and draft text are available. <br>
Risk: Target-journal adaptation can drift into imitation or unsupported content if target papers are treated as source material. <br>
Mitigation: Use target papers only to model section functions and information order, validate target-journal models with the included script, and keep target-paper claims, citations, mechanisms, and wording out of the manuscript. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yila-ai/skills/science-research-writing) <br>
- [Yila-AI/sci-ssci-skills](https://github.com/Yila-AI/sci-ssci-skills) <br>
- [Input and output contract](references/input-output-contract.md) <br>
- [Certainty and claim-strength contract](references/certainty-and-claim-strength.md) <br>
- [Target-Journal Model Builder](references/reverse-engineering-protocol.md) <br>
- [Section Function Map](assets/section-function-map.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with manuscript draft text, diagnosis, organization notes, author confirmation, next-step guidance, and optional local validation outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local Python validation scripts for draft invariants or target-journal model structure when the required user-supplied files are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
