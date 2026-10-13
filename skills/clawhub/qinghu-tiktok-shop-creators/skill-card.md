## Description:

Queries TikTok Shop creators associated with a seller ID through Qinghu's creator-list tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shop operators and analysts use this skill to identify creators promoting a TikTok Shop seller, including competitors' creator partnerships. It returns an associated-creator list, not detailed creator profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setting up the skill can install or upgrade qhkit and Node and change PATH or shell configuration.

Mitigation: Use a controlled environment and review installation commands and configuration changes before allowing them.

Risk: The skill needs a Qinghu API token.

Mitigation: Have the user supply the token through the supported configuration or environment variable and avoid exposing it in responses.

Risk: Creator-list calls consume Qinghu credits, with higher charges possible for larger results.

Mitigation: Check the current estimate, disclose expected charges, and obtain user approval before paid calls or larger batches.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-tiktok-shop-creators)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise prose with a short preview; tabular file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the credits spent on paid calls; creator details require a separate query.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
