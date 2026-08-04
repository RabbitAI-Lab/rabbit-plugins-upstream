## Description: <br>
Net Deep Research helps an agent perform explicit, multi-round web research with source reputation scoring, URL safety checks, conflict handling, and structured evidence feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[h4444433333](https://clawhub.ai/user/h4444433333) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers invoke this skill with `/net-deep-research` when they need an agent to research current or source-sensitive questions across multiple public web sources, compare evidence, explain uncertainty, and return a cited Markdown answer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can transmit research-related source domains, URLs, cited-source metadata, evidence links, query classification, and quality signals to a third-party backend. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid private or internal URLs and sensitive investigations unless the disclosure boundary is approved. <br>
Risk: Explicit high-sensitivity diagnostics or vote actions may send raw query text, full answer text, or trust and untrust votes when separately requested. <br>
Mitigation: Keep those modes opt-in and confirm the user intends to share the additional diagnostic or vote data before using them. <br>


## Reference(s): <br>
- [Research Playbook](artifact/references/research-playbook.md) <br>
- [Feedback Contract](artifact/references/feedback-contract.md) <br>
- [Source Scoring](artifact/references/source-scoring.md) <br>
- [Writing Rules](artifact/references/writing-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, API calls] <br>
**Output Format:** [Markdown answer with source notes, uncertainty, and optional structured JSON feedback to the backend] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Triggered only by `/net-deep-research`; default feedback excludes raw query text and final answer text.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
