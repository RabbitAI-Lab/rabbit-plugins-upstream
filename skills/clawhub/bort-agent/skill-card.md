## Description: <br>
BORT Agent (BAP-578) helps agents send messages to BORT AI agents, check runtime status, and query BAP-578 on-chain identity data on BNB Chain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsu-j](https://clawhub.ai/user/tsu-j) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to communicate with configured BORT agent runtimes, verify agent status, and read public BAP-578 identity state from BNB Smart Chain. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Messages are sent to whichever BORT runtime URL the user configures. <br>
Mitigation: Verify BORT_RUNTIME_URL before sending messages and avoid sending secrets or sensitive personal information to untrusted runtimes. <br>
Risk: Agent responses and public blockchain data are external content. <br>
Mitigation: Treat responses as untrusted and independently verify important on-chain identity or status information. <br>
Risk: BNB Smart Chain queries depend on the configured RPC endpoint. <br>
Mitigation: Verify BNB_RPC_URL and retry against a trusted endpoint when query results are unexpected. <br>


## Reference(s): <br>
- [BAP-578 Overview](references/bap578-overview.md) <br>
- [BORT Agent Skill Page](https://clawhub.ai/tsu-j/skills/bort-agent) <br>
- [BAP-578 Contract on BSCScan](https://bscscan.com/address/0x15b15df2ffff6653c21c11b93fb8a7718ce854ce) <br>
- [Platform Registry on BSCScan](https://bscscan.com/address/0x985eae300107a838c1aB154371188e0De5a87316) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API or blockchain query responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses BORT_RUNTIME_URL for runtime calls and BNB_RPC_URL for BNB Smart Chain reads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
