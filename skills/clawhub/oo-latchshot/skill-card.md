## Description: <br>
Latchshot lets agents capture public web pages as image or PDF artifacts and read account usage through an OOMOL-connected Latchshot account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Latchshot through OOMOL's oo CLI, including capturing public web pages and checking usage, quota, and plan status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Page capture creates and uploads a rendered artifact, which can expose sensitive content if the target URL is private or contains confidential information. <br>
Mitigation: Confirm the target URL and expected artifact type before capturing pages that may reveal private or sensitive content. <br>


## Reference(s): <br>
- [ClawHub Latchshot Skill](https://clawhub.ai/oomol/skills/oo-latchshot) <br>
- [Latchshot Homepage](https://latchshot.fly.dev) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include action data and a meta.executionId when run through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
