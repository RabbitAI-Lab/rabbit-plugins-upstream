## Description:

Checks draft text for sensitive or prohibited terms, platform-specific content risks, compliance concerns, and safer rewrite suggestions for Xiaohongshu, Douyin, Kuaishou, and general text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and agents use this skill to check draft copy for sensitive terms, prohibited wording, platform risk signals, and safer rewrite options before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text and structured results are sent to and retained by SocialDataX for history, billing, and troubleshooting.

Mitigation: Avoid submitting confidential drafts unless that data handling is acceptable for the user or organization.

Risk: API credentials could be exposed if supplied outside the documented environment variable flow.

Mitigation: Provide the API key only through SOCIALDATAX_API_KEY and do not include it in prompts, shell history examples, or skill text.

Risk: The current release checks text only and does not support image sensitivity checks.

Mitigation: Use this skill only for text review and route image review needs to a separate supported capability.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-sensitive-check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and the node/npm-based socialdatax-skills package; checks only text in the current release.]

## Skill Version(s):

0.1.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
