## Description: <br>
VerifiedEmail (verified.email) lets an agent inspect VerifiedEmail schemas and run VerifiedEmail connector actions for searching, reading, entitlement lookup, and synchronous email verification through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to operate VerifiedEmail through an OOMOL-connected account, including listing verification resources, checking credit entitlements, retrieving downloads or lists, and verifying one to ten email addresses synchronously. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email addresses submitted for verification are sent to VerifiedEmail through the OOMOL connector. <br>
Mitigation: Use the skill only for intended VerifiedEmail workflows and review requests before verifying sensitive contact lists. <br>
Risk: Credentials or account connections may grant access to VerifiedEmail data and credits. <br>
Mitigation: Keep API credentials scoped to VerifiedEmail and rely on the OOMOL-connected account flow rather than exposing raw tokens to the agent. <br>
Risk: Actions that change service state could affect VerifiedEmail resources if added or tagged in future connector schemas. <br>
Mitigation: Fetch the live action schema before constructing payloads and require explicit user confirmation for actions marked write or destructive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-verifiedemail) <br>
- [VerifiedEmail homepage](https://verified.email) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
