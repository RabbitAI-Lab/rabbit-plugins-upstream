## Description: <br>
A Chinese-language pet-chain tax compliance assistant for tax policy Q&A, risk self-checks, case references, report templates, and practical guidance across pet medical, food, grooming, boarding, training, franchise, import, live animal sale, invoicing, and private-account revenue scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet-chain operators, tax and finance staff, compliance consultants, and agent users use this skill to ask Chinese tax compliance questions, run lightweight risk self-checks, and generate structured remediation guidance or compliance report drafts for pet-chain business scenarios. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check metrics may be sent to the publisher's cloud service. <br>
Mitigation: Avoid entering confidential business, financial, customer, or identity data unless the publisher's data handling and retention terms are acceptable; use offline fallback guidance for sensitive exploratory work. <br>
Risk: The skill can register and store local API credentials for the cloud-backed tax service. <br>
Mitigation: Review where credentials are stored, protect local user data directories, remove credentials after evaluation if not needed, and avoid running the skill on shared or unmanaged machines. <br>
Risk: Setup code can modify host agent MCP configuration when write mode is explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode until configuration changes are reviewed, and inspect backups or diffs before enabling automatic MCP configuration. <br>
Risk: Tax outputs are advisory and may be incomplete or stale for a specific taxpayer, locality, or filing position. <br>
Mitigation: Verify material conclusions against current official tax authority sources and qualified tax or legal professionals before filing, remediation, dispute handling, or audit response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-pet-chain) <br>
- [Pet-chain compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_pet_chain.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Chinese-language Markdown or plain text with structured checklists, risk ratings, remediation steps, report drafts, links, and optional configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions and self-check inputs through cloud MCP tools, with offline fallback guidance when cloud access is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
