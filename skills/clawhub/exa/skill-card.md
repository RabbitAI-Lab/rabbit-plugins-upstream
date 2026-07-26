## Description: <br>
Neural web search and code context via Exa AI API. Requires EXA_API_KEY. Use for finding documentation, code examples, research papers, or company info. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fardeenxyz](https://clawhub.ai/user/fardeenxyz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to query Exa for web search results, code context, documentation, research papers, company information, and full-text content from supplied URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, URLs, and requested page content are sent to Exa. <br>
Mitigation: Do not include secrets, private source code, internal URLs, or confidential identifiers in queries or URL content requests. <br>
Risk: The skill depends on an EXA_API_KEY credential. <br>
Mitigation: Keep EXA_API_KEY private and provide it only through the execution environment. <br>


## Reference(s): <br>
- [Exa API Keys Dashboard](https://dashboard.exa.ai/api-keys) <br>
- [ClawHub Skill Page](https://clawhub.ai/fardeenxyz/skills/exa) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON API responses and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires EXA_API_KEY and sends search queries, URLs, and requested page content to Exa.] <br>

## Skill Version(s): <br>
0.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
