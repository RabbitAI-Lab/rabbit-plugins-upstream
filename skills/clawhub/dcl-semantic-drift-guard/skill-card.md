## Description: <br>
Detects semantic hallucinations and context drift by comparing LLM output against an authoritative source and returning a structured verdict with drift details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daririnch](https://clawhub.ai/user/daririnch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams responsible for RAG, legal, medical, financial, support, or policy-sensitive AI outputs use this skill to check whether generated text is grounded in a source document or retrieved knowledge base before delivery or commit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privacy and locality claims can be misunderstood because the artifact also documents a remote knowledge-base mode and an optional paid MCP pre-check. <br>
Mitigation: Use local context mode for sensitive documents unless remote processing is explicitly intended and reviewed. <br>
Risk: Remote knowledge-base or paid MCP use may send text, queries, hashes, or verdict metadata outside the local agent context. <br>
Mitigation: Document and approve the selected mode before use, and explain what data or hashes leave the agent for that mode. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daririnch/skills/dcl-semantic-drift-guard) <br>
- [DCL Trust Oracle MCP server](https://mcp.fronesislabs.com/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON audit record with verdict, confidence, drift items, transaction hash, and timestamp, with explanatory text or guidance when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Verdicts are IN_COMMIT or HALLUCINATION_DRIFT; strictness can be strict, balanced, or lenient.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
