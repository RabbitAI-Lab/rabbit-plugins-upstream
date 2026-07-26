## Description: <br>
Author durable Lethe memory through Charon as a proposer principal using owned refs, CAS changesets, semantic operations, and merge proposals for independent review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mentholmike](https://clawhub.ai/user/mentholmike) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to draft durable project memory through Charon while preserving separation between authorship and independent review. It guides proposer principals through orienting, branching, committing, verifying, and proposing memory changes without reviewing or merging them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Proposed memory can become persistent after reviewer approval. <br>
Mitigation: Install only where durable project memory drafting is intended, confirm the proposer credential is limited to the target project, and require independent review before merge. <br>
Risk: Memory proposals could include credentials, private reasoning, unnecessary personal data, or unverified claims. <br>
Mitigation: Follow the skill's hard rules: do not store sensitive content, treat recalled memory as evidence, and re-verify changing facts against source systems. <br>
Risk: A proposer may try to bypass authorization, validation, or stale-branch protections after an error. <br>
Mitigation: Use owned refs, exact project grants, CAS expected heads, unique idempotency keys, and report 401 or 403 authorization failures instead of switching identities, refs, or projects. <br>


## Reference(s): <br>
- [Charon Proposer on ClawHub](https://clawhub.ai/mentholmike/skills/charon-proposer) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command and tool-name references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces proposer workflow instructions and safety constraints for durable memory authoring.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
