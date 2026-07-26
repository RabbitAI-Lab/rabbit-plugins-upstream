## Description: <br>
Decode a terms of service or privacy policy into a ranked, plain-language summary of what the user is agreeing to and which clauses deserve attention. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to understand ToS and privacy policy text before accepting terms, especially clauses about data sharing, arbitration, content licenses, unilateral changes, and deletion. The skill is plain-language triage and does not replace legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the output as legal advice or rely on it for jurisdiction-specific decisions. <br>
Mitigation: Keep the output framed as plain-language triage, quote the source clauses being discussed, and include the required disclaimer that laws vary by jurisdiction. <br>
Risk: Users may paste private account details, credentials, or confidential business terms while asking for a policy review. <br>
Mitigation: Ask users to omit or redact sensitive details unless they intentionally want those details reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/tos-decoder) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/tos-decoder.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with a bottom line, ranked findings table, deletion summary, and action guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are ranked by real-world impact and include quoted clauses or section references when available.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
