## Description: <br>
Mandatory authorize-before-mutate for production SQL; use whenever the agent would run INSERT, UPDATE, DELETE, DDL, ALTER, TRUNCATE, or DROP against a real database, Postgres MCP, Supabase, or any SQL write tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cabbageandtea](https://clawhub.ai/user/cabbageandtea) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to require SQLGuard authorization before mutating production or non-throwaway SQL databases. It gates execution on a paid PASS receipt and successful verification, with fail-closed behavior when payment or verification fails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Production SQL writes depend on an external SQLGuard authorization and paid receipt flow. <br>
Mitigation: Confirm the SQLGuard workflow, vendor relationship, payment amounts, and availability expectations are acceptable before using the skill for database operations. <br>
Risk: Bypassing a failed payment or failed verification could allow unauthorized database mutation. <br>
Mitigation: Follow the skill's fail-closed rule: settle payment failures, require verify to return ok: true, and do not execute when status is FAIL. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cabbageandtea/skills/sqlguard-authorize) <br>
- [SQLGuard](https://sqlguard.io) <br>
- [SQLGuard Gateway](https://sqlguard.io/gateway) <br>
- [SQLGuard Gateway Documentation](https://sqlguard.io/GATEWAY.md) <br>
- [SQLGuard MCP](https://sqlguard.io/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands] <br>
**Output Format:** [Markdown instructions with inline endpoint, payment, and MCP tool references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fail-closed authorization workflow for production SQL mutations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
