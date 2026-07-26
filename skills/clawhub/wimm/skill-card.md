## Description: <br>
Manage your money with WIMM — add and search transactions, check balances, set budgets, and get spending reports from chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ipostny](https://clawhub.ai/user/ipostny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users with WIMM PRO accounts use this skill to manage their own WIMM personal finance records from chat, including accounts, transactions, budgets, categories, tags, balances, and spending reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a WIMM API key that can read financial data and, after confirmation, create, edit, or delete records in the user's WIMM account. <br>
Mitigation: Install only if the user trusts WIMM, keep WIMM_API_KEY private, and review each write confirmation carefully before approval. <br>
Risk: Incorrect account, category, transaction, budget, or tag identifiers could affect the wrong financial records. <br>
Mitigation: Look up real identifiers before using them and do not proceed with POST, PATCH, or DELETE requests until the user confirms the exact change. <br>


## Reference(s): <br>
- [WIMM MCP documentation](https://wimm.my/docs/mcp) <br>
- [ClawHub skill page](https://clawhub.ai/ipostny/skills/wimm) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WIMM_API_KEY, curl, and jq; write operations require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
