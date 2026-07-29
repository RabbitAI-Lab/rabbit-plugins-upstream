## Description: <br>
Autoblogging.ai helps agents inspect Autoblogging.ai action schemas, create article generation jobs after confirmation, and fetch article job status through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Autoblogging.ai from an agent workflow: create article generation jobs after confirming payloads and fetch article status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating articles may consume Autoblogging.ai or OOMOL credits. <br>
Mitigation: Confirm the exact article payload and intended effect before running the create_article action. <br>
Risk: Setup commands, login, or connection URLs could affect the user's OOMOL environment if run unnecessarily. <br>
Mitigation: Run oo CLI install, login, or connection steps only after a connector command fails for the matching setup reason and the user trusts the OOMOL setup path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-autoblogger) <br>
- [Autoblogging.ai homepage](https://autoblogging.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before payload construction; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
