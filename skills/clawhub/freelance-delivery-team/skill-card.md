## Description:

Scouts, qualifies, proposes, delivers fixed-scope freelance jobs, and monitors payments using a coordinated five-role agent team.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Freelancers and delivery operators use this agent team to find fixed-scope online work, qualify opportunities, draft truthful proposals, execute approved deliverables, and track payment signals. The workflow is intended for supervised use where proposals, delivery, and payment-related decisions remain approval-gated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The team is expected to use web, file, memory, and command tools while scouting jobs, drafting proposals, completing work, and tracking payment.

Mitigation: Run it with supervised access to only the relevant workspaces and job-related files, and review proposals and deliverables before external submission.

Risk: Payment monitoring could be confused with authority to initiate or approve money movement.

Mitigation: Keep payment-related decisions approval-gated and do not grant bank-transfer authority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/freelance-delivery-team)
- [T3raTech Solutions publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text responses, with generated or modified workspace files and shell commands when approved work requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposal submission, final delivery, and payment-related actions should remain approval-gated.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
