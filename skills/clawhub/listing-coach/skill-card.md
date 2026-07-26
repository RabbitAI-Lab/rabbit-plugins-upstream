## Description: <br>
Query the configured real estate Listing Coach knowledge base and return the exact retrieval output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woowonjae1](https://clawhub.ai/user/woowonjae1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and real estate professionals use this skill to retrieve listing-coach scripts, objection-handling language, expired-listing scripts, and FSBO scripts from a configured knowledge base without rewriting the retrieved text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User queries and retrieved coaching content are sent to a configured external knowledge-base service. <br>
Mitigation: Use only with content appropriate for that external service and avoid submitting sensitive client or personal information unless the service is approved for it. <br>
Risk: The security summary reports signed API requests over plain HTTP. <br>
Mitigation: Prefer a version or configuration that requires HTTPS for the knowledge-base endpoint before production use. <br>
Risk: The security summary reports that retrieved results are stored in a temporary file. <br>
Mitigation: Review local temporary-file handling and cleanup expectations before deployment, especially on shared systems. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Exact retrieved text, usually Markdown or plain text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the retrieval result exactly; retrieved content may be written to a temporary Markdown file before the agent reads and returns it.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
