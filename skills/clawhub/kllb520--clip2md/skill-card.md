## Description:

Clip2MD lets an agent configure an access token, submit web pages or article URLs as Markdown clipping tasks, check quota, query task status, and wait for completion or failure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kllb520](https://clawhub.ai/user/kllb520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate the clip2md service from an agent, saving web pages as Markdown clipping tasks and checking quota or task progress without manually calling the API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bearer token is stored locally in ~/.clip2md/config.json.

Mitigation: Use the skill only in a trusted local environment and ensure the config file is readable only by the current user.

Risk: CLIP2MD_API_BASE can redirect API requests, including the bearer token, to an environment-selected host.

Mitigation: Do not set CLIP2MD_API_BASE except for trusted test or private deployments.

Risk: Submitting URLs can consume clip2md quota or disclose the submitted page URL to the clip2md service.

Mitigation: Require explicit user approval before submitting URLs and report quota or permission failures without retry loops.

## Reference(s):

- [Clip2MD Skill Page](https://clawhub.ai/kllb520/skills/clip2md)
- [Publisher Profile](https://clawhub.ai/user/kllb520)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or concise text summaries with inline shell commands and task status fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report task id, status, quota, title or error, and whether Markdown is ready; full Markdown content is shown only when explicitly requested.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; package.json reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
