## Description: <br>
Tax Pet Chain helps users evaluate China-focused tax compliance questions, risk indicators, case patterns, report templates, and practical guidance for pet-chain businesses across supply, retail, grooming, veterinary care, boarding, training, franchising, live-animal sales, and imported pet food. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax teams, and compliance reviewers use this skill to ask pet-chain tax questions, run self-checks, identify risk items, and draft practical remediation or compliance-report content. It is not a substitute for licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Avoid entering client-confidential, taxpayer-identifying, or sensitive business data unless the publisher's consent, storage, retention, and deletion terms are acceptable. <br>
Risk: API keys may be stored locally by the Python client and in browser localStorage by the web workflow. <br>
Mitigation: Treat the local user profile and browser profile as credential-bearing, and clear stored keys when the skill is no longer used. <br>
Risk: The skill can optionally modify MCP client configuration. <br>
Mitigation: Review configuration changes before enabling automatic setup and keep the generated backup files for rollback. <br>
Risk: Fallback behavior may send search queries to public search engines. <br>
Mitigation: Do not use sensitive taxpayer, customer, or transaction details in prompts that could trigger fallback search. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-pet-chain) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Pet-chain compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_pet_chain.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with structured checklists, risk assessments, report templates, and optional configuration commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services and a browser self-check page; offline fallback guidance is included.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
