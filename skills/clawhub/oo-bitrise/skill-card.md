## Description: <br>
Bitrise (bitrise.io) helps agents read Bitrise apps and builds, inspect live connector schemas, and trigger Bitrise builds or pipelines through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and CI operators use this skill to list Bitrise apps, browse or retrieve builds, and trigger builds or pipelines from an authenticated OOMOL-connected Bitrise account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read operations may expose Bitrise app and build data to OOMOL as the intermediary connector. <br>
Mitigation: Install and use the skill only when the account owner accepts OOMOL-mediated access to Bitrise data. <br>
Risk: Triggering Bitrise builds or pipelines can change CI state or consume CI resources. <br>
Mitigation: Confirm the exact write payload and intended effect with the user before running build-trigger actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bitrise) <br>
- [Bitrise Homepage](https://bitrise.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the oo CLI connector schema before action execution and returns connector responses as JSON when commands are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
