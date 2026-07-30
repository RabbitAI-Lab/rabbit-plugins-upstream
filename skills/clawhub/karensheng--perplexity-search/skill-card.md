## Description: <br>
Perplexity 搜索 helps agents run grounded Perplexity web search and research through SELAT, returning source-backed results and guidance for cost-confirmed paid calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[karensheng](https://clawhub.ai/user/karensheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need an agent to search the web, research current topics, or prepare cited answers using Perplexity through SELAT. It is suited for source-backed research workflows where the user can review a live price quote before any paid call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid searches and escalated research calls spend USDC from the user's own wallet. <br>
Mitigation: Run the documented dry run first, show the live quote, and get explicit user approval before wallet setup or each paid call. <br>
Risk: Search queries are sent to SELAT and Perplexity as part of the web research workflow. <br>
Mitigation: Confirm the user is comfortable sending the query to those services before installation or execution. <br>
Risk: Private keys or wallet secrets could be exposed if handled outside the documented CLI flow. <br>
Mitigation: Do not ask for, paste, store, or relay private keys; use the CLI's wallet integration only. <br>


## Reference(s): <br>
- [Perplexity Search Skill Homepage](https://github.com/SELAT-AI/selat-skills/tree/main/skills/perplexity-search) <br>
- [SELAT Skills Documentation](https://github.com/SELAT-AI/selat-skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/karensheng/skills/perplexity-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and cited source links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output should be synthesized into concise answers with inline citations, recency context, and the reported cost when a paid call is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
