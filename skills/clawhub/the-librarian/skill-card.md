## Description: <br>
Build and search knowledge bases using Supabase for conversations and curated knowledge, or TurboVec for offline and resource-constrained document search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rochyroch](https://clawhub.ai/user/rochyroch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to build searchable private knowledge bases, query conversations or knowledge entries, and create compact document indexes for local retrieval workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed around privileged Supabase service-role access and sensitive WhatsApp or knowledge-base data. <br>
Mitigation: Install only in environments where those credentials and datasets are intentionally available to the agent, and review access before deployment. <br>
Risk: Document text and search queries may be sent to an embedding API endpoint. <br>
Mitigation: Use a local trusted Ollama endpoint for sensitive content, and avoid remote embedding APIs unless their data handling is acceptable. <br>
Risk: Index directories can contain full document text and search metadata. <br>
Mitigation: Treat generated indexes as sensitive data, share them only with trusted parties, and rebuild untrusted legacy indexes before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rochyroch/skills/the-librarian) <br>
- [RandTrad Consulting](https://www.randtradconsulting.com) <br>
- [TurboVec Quantization Explained](references/quantization.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, SQL, Python, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce JSON search results when the search script is run with JSON output.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
