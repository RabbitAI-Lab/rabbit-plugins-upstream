## Description: <br>
Harden a ZK-Bankir sovereign banking deployment with guided threat model checks, hash-chain integrity verification, dependency scanning, access control review, and runbook validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill to audit local ZK-Bankir deployments before deployment, during routine hardening, or during incident response. It helps them verify ledger integrity, dependencies, policy tiers, runbook coverage, and related safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports a live destroy command used as a verification step without clear production safeguards. <br>
Mitigation: Review the command before use and run destructive validation only in an isolated staging or test environment with disposable records; use code inspection or dry-run validation for production systems. <br>


## Reference(s): <br>
- [ZK-Bankir project homepage](https://gitlab.com/1Beekeeper/zk-bankir) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, ruby, and bundle on Linux or Darwin with access to a local ZK-Bankir project.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
