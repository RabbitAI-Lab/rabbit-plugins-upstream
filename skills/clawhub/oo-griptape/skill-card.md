## Description: <br>
Operates Griptape Cloud through an OOMOL-connected account using the oo CLI for assistant, run, and organization workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Griptape connector schemas and manage Griptape Cloud assistants, runs, and organizations through OOMOL's oo CLI. It supports read workflows plus confirmed write and destructive lifecycle actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, cancel, and delete Griptape resources. <br>
Mitigation: Require confirmation of the exact target, payload, and expected effect before write or destructive actions. <br>
Risk: Connected account scopes may allow access to or changes in Griptape data. <br>
Mitigation: Install only for intended Griptape account operations, review connection scopes, and require confirmation before state-changing actions. <br>


## Reference(s): <br>
- [Griptape homepage](https://www.griptape.ai) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-griptape) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
