## Description: <br>
Manage Austrian Post (post.at) deliveries - list packages, check delivery status, set delivery place preferences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krausefx](https://clawhub.ai/user/krausefx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage Austrian Post deliveries through the post-at CLI, including listing deliveries, checking delivery details, and setting delivery place preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: post.at credentials may be exposed if passwords are passed directly on the command line or stored in unprotected environments. <br>
Mitigation: Use POST_AT_USERNAME and POST_AT_PASSWORD from a protected environment or secret manager. <br>
Risk: Routing or delivery-place commands can change where a real package is delivered. <br>
Mitigation: Confirm the tracking number, place option, and description before running routing commands. <br>
Risk: The skill depends on an external post-at CLI and Node runtime. <br>
Mitigation: Install the CLI only from the intended source and verify that node is available before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/krausefx/skills/post-at) <br>
- [post-at CLI Homepage](https://github.com/krausefx/post-at-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide use of JSON output from the post-at CLI for scripting and automation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
