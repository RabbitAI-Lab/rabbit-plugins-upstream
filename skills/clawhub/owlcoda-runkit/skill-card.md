## Description:

OwlCoda RunKit helps agents coordinate large, receipt-backed projects through project-owned artifacts, leases, handoffs, verification gates, and recovery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yeemio](https://clawhub.ai/user/yeemio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multi-agent software work with durable project artifacts instead of chat history. It supports task assignment, handoff, deferred verification, receipt capture, foreign-project shadow verification, and ready-for-commit evidence while keeping release authority separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may install or trust the external owlrunkit package without confirming package provenance.

Mitigation: Verify the external owlrunkit package provenance and registry adoption evidence before installation or use.

Risk: Users may treat RunKit coordination state as authorization for Git, release, deployment, credential, destructive, or foreign-project write actions.

Mitigation: Require separate explicit authority for those actions and treat RunKit receipts as evidence records only.

Risk: Project coordination files may be confused with product source or included in delivery scope.

Mitigation: Keep `.owlcoda/runkit/**` as local runtime truth and exclude it from product source, leases, profiles, and delivery changed files.

## Reference(s):

- [OwlCoda RunKit source homepage](https://github.com/yeemio/owlcodaS)
- [OwlCoda RunKit Contract v0.2](artifact/references/contract-v0.2.md)
- [OwlCoda RunKit Contract v0.1](artifact/references/contract-v0.1.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses project-local evidence, lease, packet, receipt, and verification artifacts; does not itself grant Git, release, deployment, credential, destructive, or foreign-write authority.]

## Skill Version(s):

0.22.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
