## Description:

BookOrigin DOCX Review performs local read-only ZIP/DOCX structure preflight checks on authorized DOCX files and produces advisory review packages bound to source hashes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reviewers, and documentation teams use this skill to check an authorized DOCX for ZIP/DOCX safety and limited textbook-structure signals, then package human review decisions with source-hash and event-chain consistency checks. It is advisory only and does not approve, sign, modify, or validate document quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat ZIP/DOCX structure preflight as malware scanning, Office rendering validation, legal approval, or document-quality verification.

Mitigation: Use this skill only as a local advisory precheck and rely on separate malware scanning, rendering review, legal review, and quality assurance where those decisions matter.

Risk: Users may treat an advisory review package as an approval, signature, identity assertion, or tamper-proof chain of custody.

Mitigation: Require a separate approval, identity, signature, and records-management process for authoritative decisions.

Risk: The skill reads local DOCX and JSON files supplied by the caller.

Mitigation: Run it only on files the caller is authorized to process and handle the resulting hashes, manifests, and decisions according to the applicable document-handling policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dongsheng123132/skills/bookorigin-docx-review)
- [Artifact Skill Instructions](artifact/SKILL.md)
- [Action Contract](artifact/action-contract.json)
- [Runtime Manifest](artifact/skill.json)

## Skill Output:

**Output Type(s):** [JSON, guidance]

**Output Format:** [Single-line JSON objects containing preflight findings, review-case templates, or advisory review-package manifests.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs omit absolute paths, source text, DOCX bytes, and secrets; findings and review packages are advisory only.]

## Skill Version(s):

1.0.0 (source: evidence release and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
