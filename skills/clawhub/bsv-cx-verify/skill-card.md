## Description:

Verifies Bitcoin SV Merkle proofs in TSC, BEEF, or BUMP formats against bsv.cx self-synced block headers and can fetch BEEF or BUMP proofs for a transaction ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsv-cx](https://clawhub.ai/user/bsv-cx)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to check whether Bitcoin SV transaction inclusion proofs are confirmed, rejected, or inconclusive, and to retrieve BEEF or BUMP proof material for a transaction ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transaction IDs or proof material submitted for verification are sent to bsv.cx.

Mitigation: Only send public transaction IDs or proof material you are comfortable disclosing to bsv.cx; never provide private keys, seed phrases, wallet credentials, or unrelated confidential data.

Risk: A proof can be inconclusive when bsv.cx has not synced the relevant block header yet.

Mitigation: Treat inconclusive responses as not confirmed by this check and retry after the service tip has advanced past the proof height.

Risk: The live bsv.cx API contract may differ from examples embedded in the skill text.

Mitigation: Check the live GET /spv contract before relying on request or response shapes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bsv-cx/skills/bsv-cx-verify)
- [bsv.cx SPV live contract](https://bsv.cx/spv)
- [bsv.cx service map](https://bsv.cx/)
- [bsv-cx publisher profile](https://clawhub.ai/user/bsv-cx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, markdown, configuration]

**Output Format:** [Markdown with inline bash, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only verification guidance and HTTP request examples; requires curl and jq for the documented shell workflows.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
