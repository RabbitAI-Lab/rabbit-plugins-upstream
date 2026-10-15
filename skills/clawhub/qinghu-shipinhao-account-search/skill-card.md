## Description:

Searches videos within a specified WeChat Channels account by keyword using Qinghu AI's paid data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

People researching a WeChat Channels creator's videos use this skill to find videos in that account matching a keyword and receive a concise summary of the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests consume credits on an external data service.

Mitigation: Check the current price and obtain approval before paid calls; report actual credits used.

Risk: Setup instructions may install or upgrade software and modify the user's environment.

Mitigation: Prefer a pre-provisioned or sandboxed qhkit installation; approve installs, upgrades, and shell startup changes explicitly.

Risk: Using the service requires an iqinghu API token.

Mitigation: Configure the token only in a trusted environment and avoid exposing it in shared outputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-account-search)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise result summary; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a creator username and keyword; paid queries require user approval.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
