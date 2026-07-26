## Description: <br>
Publish agent-generated artifacts to durable Tunly links with explicit privacy and immutable versions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seaguest](https://clawhub.ai/user/seaguest) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to publish generated reports, dashboards, prototypes, evidence bundles, static sites, and other browser-readable artifacts as durable Tunly links with account-only defaults and immutable versions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user could publish secrets, credentials, private keys, environment files, dependency directories, or unrelated local data by choosing the wrong artifact path. <br>
Mitigation: Review the artifact directory before publishing and keep customer, project, operational, personal, and unreleased content account-only unless the user explicitly approves public access. <br>
Risk: The skill can use Tunly account authorization or API-key based access for operational publishing. <br>
Mitigation: Use scoped API tokens where available, run `tunly auth status` before publishing, and review publish commands before approving them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/seaguest/skills/tunly-artifact-share) <br>
- [Tunly CLI install script](https://tunly.io/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and a concise publish status response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports the latest URL, immutable version URL or revision, access mode, and verification result after publishing.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
