## Description: <br>
Fidacy Artifact Anchoring helps agents hash selected local documents, anchor only the digest through Fidacy, and return a signed receipt that can be publicly verified later. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fidacy](https://clawhub.ai/user/fidacy) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers, employees, and external users can use this skill when a final contract, invoice, claim document, report, prescription, or media artifact needs an existence and integrity proof without uploading the file itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on Fidacy's external MCP server and an API key. <br>
Mitigation: Install and configure it only in environments where use of the Fidacy service and credential handling are approved. <br>
Risk: Anchoring proves a file matches a prior hash, not that the document contents are true, fair, valid, or legally binding. <br>
Mitigation: Use the receipt as integrity evidence only, and keep separate review processes for content accuracy, legal effect, and business approval. <br>
Risk: The proof applies to the specific file selected for hashing. <br>
Mitigation: Anchor only final artifacts intentionally selected for proofing, and re-verify the exact file or digest before relying on the receipt. <br>


## Reference(s): <br>
- [Fidacy Verification Page](https://fidacy.com/verify) <br>
- [Fidacy Artifact Verification API](https://api.fidacy.com/v1/verify/artifact?sha256=<hex>) <br>
- [Fidacy Signup](https://app.fidacy.com/signup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with tool names, commands, verification links, and receipt/status descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill produces document-integrity guidance and directs the agent to use Fidacy MCP tools; it does not store or return the source artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
