## Description: <br>
Operate Flagsmith through an OOMOL-connected account to inspect feature flags, evaluate identity flags and traits, and identify users through connector actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to access a connected Flagsmith environment from an agent, including listing flags, retrieving flag values, and evaluating or identifying identities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the identity action can change Flagsmith traits even though it is not tagged as a write action. <br>
Mitigation: Require explicit user confirmation before running identify_identity with trait-setting data. <br>


## Reference(s): <br>
- [Flagsmith homepage](https://www.flagsmith.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Flagsmith skill](https://clawhub.ai/oomol/skills/oo-flagsmith) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before running Flagsmith actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
