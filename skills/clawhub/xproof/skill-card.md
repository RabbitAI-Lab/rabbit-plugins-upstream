## Description: <br>
Certify what an agent decided before acting and what it produced afterward, creating a 4W audit trail on MultiversX with a Base violations layer and trust score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jasonxkensei](https://clawhub.ai/user/jasonxkensei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to hash reasoning and results locally, anchor proof metadata through xProof APIs or MCP, and verify public audit records for compliance or incident review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Proof records are permanent and public, and submitted filenames, hashes, author names, or audit context may reveal sensitive or correlatable information. <br>
Mitigation: Hash content locally, submit only non-sensitive metadata, and require review before anchoring records that may expose private or regulated information. <br>
Risk: x402 mode can let an autonomous agent spend USDC on Base when creating proofs. <br>
Mitigation: Enable x402 only intentionally, configure spending caps, and require human approval for batch, high-frequency, or threshold-exceeding certification workflows. <br>
Risk: API keys can authorize proof creation if exposed in logs, prompts, or repositories. <br>
Mitigation: Store xProof API keys in secret management, keep them out of committed files and logs, and rotate any key that may have been disclosed. <br>
Risk: Runtime fetching of external documentation or enforcement snippets can add availability and prompt-injection risk. <br>
Mitigation: Use pinned local reference files or package versions for agent enforcement behavior and treat external documentation as install-time reference material. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jasonxkensei/skills/xproof) <br>
- [Server-Resolved GitHub Provenance](https://github.com/jasonxkensei/xproof-openclaw-skill/tree/main/xproof) <br>
- [xProof Homepage](https://xproof.app) <br>
- [xProof Agent Context](https://xproof.app/agent-context) <br>
- [Certification API](references/certification.md) <br>
- [MCP Server](references/mcp.md) <br>
- [x402 Payments](references/x402.md) <br>
- [Agent Proof Standard](https://github.com/jasonxkensei/xProof/blob/main/AGENT_PROOF_STANDARD.md) <br>
- [Base Violations Documentation](https://xproof.app/docs/base-violations) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, shell commands, API endpoints, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance centers on locally hashing content, submitting proof metadata, using API key or x402 payment flows, and verifying proof records.] <br>

## Skill Version(s): <br>
4.0.11 (source: ClawHub release metadata; artifact frontmatter lists 3.3.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
