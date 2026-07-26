## Description: <br>
Audits and hardens API credential handling (env vars, separation, rotation plan, least privilege, auditability). Use when integrating services or preparing production deployments where secrets must be managed safely. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to audit and harden credential handling for integrations and deployment preparation. It helps produce credential maps, rotation runbooks, least-privilege checklists, audit log plans, and placeholder-only environment templates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may expose real production secrets while discussing credential handling. <br>
Mitigation: Keep the workflow read-only by default and use redacted snippets or placeholders instead of real keys, tokens, or private keys. <br>
Risk: Credential-hardening guidance may be applied too broadly without confirming required operations, owners, or rotation cadence. <br>
Mitigation: Stop and ask for missing operational details before recommending scope reductions, secret injection changes, or rotation procedures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kowl64/skills/api-credentials-hygiene) <br>
- [Placeholder dotenv template example](artifact/assets/dotenv-template.example.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with structured checklists, runbooks, credential maps, and optional placeholder configuration templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Technical documentation only; placeholder templates must not contain real secrets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
