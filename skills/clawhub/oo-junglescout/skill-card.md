## Description:

Operates Jungle Scout through an OOMOL-connected account so agents can read, create, and update Jungle Scout data with the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Jungle Scout through an OOMOL-connected account for Amazon product research, keyword discovery, sales estimates, and brand share-of-voice workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-tagged Jungle Scout actions can change account state or saved analysis outputs.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

Risk: CLI installation, sign-in, and account connection steps affect the user's local environment and connected OOMOL account.

Mitigation: Run setup steps only after a matching command failure and only when the user trusts OOMOL and wants the connector enabled.

Risk: Incorrect connector payloads could produce failed or misleading Jungle Scout requests.

Mitigation: Fetch the live connector schema before building each payload and match the authoritative input contract.

## Reference(s):

- [ClawHub Jungle Scout skill page](https://clawhub.ai/oomol/skills/oo-junglescout)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Jungle Scout homepage](https://www.junglescout.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
