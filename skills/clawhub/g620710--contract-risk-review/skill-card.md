## Description:

Reviews contract text for legal risk indicators, clause gaps, unfair terms, risk level, legal basis, revision suggestions, and alternative clauses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[g620710](https://clawhub.ai/user/g620710)

### License/Terms of Use:

MIT-0

## Use Case:

External users, legal teams, procurement teams, founders, and individuals use this skill to perform preliminary contract risk screening before human legal review. It is aimed primarily at Chinese contract text across sales, service, lease, labor, cooperation, NDA, and other civil or commercial agreement types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive contract text and an API key may be sent to an external provider.

Mitigation: Use only with contracts and credentials that may be shared with this provider; redact confidential information when appropriate.

Risk: Release evidence reports a hard-coded default HTTP endpoint and unclear data handling terms.

Mitigation: Avoid the default endpoint unless it is replaced with a verified HTTPS service and clear provider terms.

Risk: Release evidence warns that the included script appears syntactically broken and inconsistent with documented usage.

Mitigation: Test the skill in an isolated environment and verify the documented commands, dependencies, and environment variables before operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/g620710/skills/contract-risk-review)
- [ClawHub Publisher Profile](https://clawhub.ai/user/g620710)
- [DeepSeek API Base URL Mentioned in Skill Documentation](https://api.deepseek.com/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text, Markdown, or JSON contract risk review reports with setup and command-line usage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CONTRACT_API_USER_KEY for normal use; review output is advisory and should be checked by a qualified professional.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
