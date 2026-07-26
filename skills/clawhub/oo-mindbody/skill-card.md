## Description: <br>
Mindbody (mindbodyonline.com) helps agents search and read Mindbody data through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect the Mindbody connector schema and run the documented list_businesses read action against a connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on OOMOL oo CLI access to a connected Mindbody account. <br>
Mitigation: Install only when users are comfortable using the oo CLI with their connected Mindbody account, and review login or CLI installation steps before running them. <br>
Risk: Future connector actions could change Mindbody state if write or destructive actions are added. <br>
Mitigation: Keep use limited to the documented list_businesses read action unless a future version explicitly documents additional actions and their effects. <br>


## Reference(s): <br>
- [ClawHub Mindbody skill page](https://clawhub.ai/oomol/skills/oo-mindbody) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Mindbody homepage](https://www.mindbodyonline.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses from action runs are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
