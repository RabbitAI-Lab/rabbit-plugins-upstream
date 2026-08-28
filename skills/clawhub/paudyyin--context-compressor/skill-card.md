## Description: <br>
A five-strategy context compression skill that reduces long agent conversations by cleaning old tool outputs, summarizing older messages, masking observations, extracting structured notes, and reserving a sub-agent delegation path. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to compress OpenAI-format message histories during long-running tasks while preserving recent context, tool-call structure, and selected decisions or findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Compressed summaries can silently rewrite conversation state or promote user-derived content into system-level context. <br>
Mitigation: Use only in integrations that preserve or explicitly exclude system and developer instructions, credentials, security-critical tool outputs, and user requirements; mark generated summaries as untrusted and user-derived where possible. <br>
Risk: Old tool outputs may be cleaned or masked, which can remove details needed for auditability or later reasoning. <br>
Mitigation: Retain source transcripts or logs outside the compressed context when workflows require traceability, debugging, or compliance review. <br>


## Reference(s): <br>
- [Threshold Configuration Reference](references/thresholds.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/context-compressor) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, configuration, guidance] <br>
**Output Format:** [Python objects and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a compressed message list plus compression statistics including token estimates, applied strategies, and reduction percentage.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
