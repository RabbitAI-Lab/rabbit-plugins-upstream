## Description: <br>
Appraises one unevaluated research method from the human-free platform by finding real papers, scoring capability and difficulty metrics, contributing verified literature, and submitting a structured evaluation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to evaluate research methods on the human-free platform with paper-backed capability and difficulty scores. It is intended for one-method-at-a-time appraisal, literature contribution, and structured submission of the evaluation result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated platform writes can affect the shared corpus and method-evaluation queue. <br>
Mitigation: Use a least-privileged platform API key and review the skill's write behavior before installation. <br>
Risk: The internal MCP endpoint may use a self-signed certificate, which can expose the platform API key if trusted without verification. <br>
Mitigation: Prefer the public TLS tunnel, or verify the internal certificate or CA through a trusted channel before use. <br>
Risk: Research method scores can become misleading if citations, abstracts, or metric evidence are invented or weakly grounded. <br>
Mitigation: Require retrieved papers with real DOI, arXiv, or URL evidence; skip unverifiable papers and lower confidence when evidence is thin. <br>


## Reference(s): <br>
- [Review Method skill page](https://clawhub.ai/zbc0315/skills/review-method) <br>
- [Connecting to the human-free platform (MCP)](reference/connecting.md) <br>
- [Appraising a research method: the 10 metrics](reference/evaluation-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, API calls, guidance] <br>
**Output Format:** [Markdown summary plus structured MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes paper citations, integer metric scores, rationales, confidence, verdict summary, and literature contribution counts.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
