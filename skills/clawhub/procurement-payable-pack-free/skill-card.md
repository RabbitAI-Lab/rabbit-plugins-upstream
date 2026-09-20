## Description:

A local procurement and payables checker that runs 14 built-in checks over user-supplied object folders, prints one conclusion line per object, and cites source files and line numbers for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, accounts payable, finance shared services, internal control, and audit teams use this skill during month-end close, vendor reconciliation, payment approval, provisional accrual cleanup, bidding, and contract payment reviews. It performs deterministic local pre-checks on exported text materials and highlights arithmetic, consistency, coverage, and line-referenced issues without replacing business approval, audit, tax, or legal judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes procurement, payable, contract, and accounting worksheets that may contain sensitive business data.

Mitigation: Run it only in an environment where local access to those text exports is acceptable, and provide the minimum worksheet extracts needed for the checks.

Risk: Users may mistake deterministic pre-check findings for an audit opinion, payment approval, or business judgment.

Mitigation: Review findings with the cited source lines and keep approval, audit, tax, legal, and payment decisions in the responsible business process.

Risk: Missing or poorly segmented input can leave checks unexecuted, which is not the same as a clean result.

Mitigation: Use one object directory per reviewed object, include the expected section headings or table files, and treat any reported unexecuted checks as coverage gaps to resolve before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/procurement-payable-pack-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact skill documentation](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON printed to stdout, with source file and line references for findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; reads user-supplied text or JSON exports and does not write result files.]

## Skill Version(s):

1.0.20 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
