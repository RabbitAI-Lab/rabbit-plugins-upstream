## Description: <br>
CallRail (callrail.com). Use this skill for CallRail searching and reading data through the OOMOL oo connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve CallRail accounts, companies, calls, and form submissions through an authenticated OOMOL-connected CallRail account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CallRail data access is routed through the OOMOL oo connector. <br>
Mitigation: Review the OOMOL CLI install and account connection flow before use, and run it only for intentional CallRail retrieval tasks. <br>
Risk: Connector commands may fail when authentication, connection scopes, credentials, or billing are not ready. <br>
Mitigation: Use the documented first-time setup and troubleshooting steps only after a matching command failure. <br>


## Reference(s): <br>
- [CallRail homepage](https://www.callrail.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
