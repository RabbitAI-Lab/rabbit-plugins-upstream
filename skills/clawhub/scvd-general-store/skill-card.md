## Description:

Guides agents through free x402 receipt verification, endpoint inspection and payment diagnosis, with optional user-authorized USDC purchases from SCVD's general store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check signed x402 artifacts, inspect payment endpoints and their history, troubleshoot purchases, and test buyers and sellers. Optional store purchases require a user's explicit spending decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live purchase can spend real USDC or be charged again after an uncertain response.

Mitigation: Require explicit authorization for the item, network and spend limit; preserve the original retry identity and recover an uncertain purchase before paying again.

Risk: Wallet secrets or optional identifying metadata could be exposed.

Mitigation: Never request private keys or seed phrases; sign with the user's authorized wallet and omit optional identifying metadata unless the user chooses to provide it.

Risk: Optional npm or MCP components run local code with potential access to files or environment variables.

Mitigation: Use free HTTPS checks when sufficient; pin optional components and run them with minimal filesystem and environment access.

Risk: A valid signature or passing check may be mistaken for proof of settlement or delivery.

Mitigation: Report each verdict's stated scope and missing evidence; verify settlement and fulfillment separately before drawing conclusions.

## Reference(s):

- [SCVD General Store on ClawHub](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [SCVD Store](https://scvd.store)
- [Verification guidance](artifact/references/verification.md)
- [Purchase and recovery guidance](artifact/references/purchases.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Code]

**Output Format:** [Text or Markdown with optional commands, code and structured verdict summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves observation dates, scope, exclusions and missing checks when reporting results.]

## Skill Version(s):

3.19.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
