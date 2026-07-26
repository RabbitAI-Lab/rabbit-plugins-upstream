## Description: <br>
Zoho Books helps agents use AgentPMT-hosted remote tool calls to list organizations and manage Zoho Books accounting records such as contacts, invoices, bills, expenses, payments, projects, time entries, and bank transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent work with Zoho Books through AgentPMT, including organization lookup, accounting record retrieval, and permission-gated writes such as invoice updates, deletes, emails, and bank matching. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-enabled Zoho Books actions can change, delete, void, email, or reconcile financial records. <br>
Mitigation: Start with read-only access, grant add/edit/delete permissions only when needed, and manually confirm the requested change before allowing accounting writes. <br>
Risk: Using the wrong organization, record, or recipient can apply an accounting action to the wrong target. <br>
Mitigation: Confirm the organization ID, record ID, recipient, and requested operation before invoice emails, voids, deletes, bank matching, or other sensitive actions. <br>


## Reference(s): <br>
- [Zoho Books on ClawHub](https://clawhub.ai/agentpmt/skills/zoho-books) <br>
- [AgentPMT Zoho Books marketplace page](https://www.agentpmt.com/marketplace/zoho-books) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What AgentPMT is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>
- [Generated Zoho Books schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration] <br>
**Output Format:** [Markdown instructions with JSON call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses organization-scoped Zoho Books actions with permission-gated add, edit, and delete operations; remote tool responses are JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
