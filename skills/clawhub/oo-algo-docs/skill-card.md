## Description: <br>
AlgoDocs lets agents read, create, and update AlgoDocs data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate AlgoDocs from an agent session: inspect schemas, list extractors, folders, and extracted data, fetch document records, check account identity, and import public document URLs after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a connected AlgoDocs account for account-scoped reads and one confirmed write action. <br>
Mitigation: Install it only when AlgoDocs account access is intended, and confirm the exact upload payload and expected effect before running write actions. <br>
Risk: Broad or vague AlgoDocs mentions could trigger connector use when the user only wants general information. <br>
Mitigation: Use the skill for explicit AlgoDocs account operations, and avoid invoking it for general AlgoDocs background questions. <br>


## Reference(s): <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [AlgoDocs homepage](https://algodocs.com) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON payload notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas before running account-scoped AlgoDocs actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
