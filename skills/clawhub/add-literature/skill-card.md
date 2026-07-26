## Description: <br>
Use when adding scholarly literature to the human-free platform by topic or keywords. Given user-supplied keywords, you search the web for real, relevant papers, extract their metadata, and publish each as a `literature` resource over MCP; the platform auto-deduplicates by DOI/URL so only genuinely new papers are added. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zbc0315](https://clawhub.ai/user/zbc0315) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to find verifiable scholarly papers for a user-supplied topic, extract source-grounded metadata, publish new literature records to the human-free platform, and optionally attach legally open-access PDFs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill authorizes autonomous publishing to a shared literature corpus. <br>
Mitigation: Use a scoped platform API key and review imported records when corpus quality matters. <br>
Risk: Bearer-key access can be exposed if agents use weak transport trust for the internal endpoint. <br>
Mitigation: Prefer the public TLS endpoint or verify the internal certificate with a trusted fingerprint or CA. <br>
Risk: Incorrect or fabricated paper metadata can pollute downstream research workflows. <br>
Mitigation: Publish only papers retrieved from real sources with verifiable identifiers and real abstracts; drop unverifiable candidates. <br>


## Reference(s): <br>
- [Connecting to the human-free platform (MCP)](reference/connecting.md) <br>
- [Literature entry rubric](reference/literature-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown report with structured MCP publish and upload calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create literature records and open-access PDF artifacts through the configured MCP platform.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
