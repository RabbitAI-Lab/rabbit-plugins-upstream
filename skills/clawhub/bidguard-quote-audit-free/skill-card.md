## Description:

Checks a bid quotation locally for line-item arithmetic mismatches and missing quantity, unit price, or total fields without requiring registration, payment, API keys, or network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement staff, and developers can use this skill to run a local mechanical audit of a single bid quotation before submission. It highlights line-item arithmetic mismatches and missing fields, while stating that other bid-review checks are outside the free version.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release suspicious because the free audit skill also directs users toward an agent-driven paid install and purchase flow that runs an unpinned external package.

Mitigation: Use the free local audit only if that behavior is acceptable, ignore the paid-upgrade flow unless independently verified, and do not paste the purchase/install prompt or run the unpinned npx command without checking the package, version, merchant, payment flow, and installed skill instructions.

Risk: The skill output is a mechanical quotation audit and not an official bid evaluation or qualification decision.

Mitigation: Treat findings as review guidance only and have qualified reviewers apply the tender documents and governing evaluation process before making submission or award decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bidguard-quote-audit-free)
- [Artifact skill definition](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON audit results with finding levels, row references, messages, advice, scope, and summary fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; exits with code 3 and no conclusion when input is insufficient.]

## Skill Version(s):

1.0.15 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
