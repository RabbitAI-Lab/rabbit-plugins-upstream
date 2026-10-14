## Description:

Generates a shareable short link for a WeChat Channels video from its numeric object ID using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert a WeChat Channels video's object ID into a shareable short link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating a link may incur paid Qinghu data calls.

Mitigation: Check the current price and obtain user consent before calling; report actual credits charged.

Risk: Setup may install or update Node and qhkit, changing the local environment.

Mitigation: Prefer trusted, preinstalled tooling and avoid unpinned npx/latest execution.

Risk: Qinghu API access requires a token.

Mitigation: Provide the token through a controlled secret mechanism rather than storing long-lived credentials casually on the host.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-share-link)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Plain text with a share URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits spent when a paid call is made.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
