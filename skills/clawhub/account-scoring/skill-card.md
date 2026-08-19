## Description:

Keeps accounts scored and tiered against a written ICP, re-scores them as accounts arrive or criteria change, and writes the score, tier, and rationale back to the CRM.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and GTM teams use this skill to keep account fit scoring current against an ICP, with CRM-visible rationale that helps sales teams decide which accounts to work first. Developers adapt the Cargo CDK resources, CRM connector, model columns, and tier thresholds before planning and deploying.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM fields or selected account model columns may be missing, causing scores or tier segments to appear successful while not being usable by reps.

Mitigation: Confirm cargo_score, cargo_tier, cargo_rationale, and cargo_last_updated_at exist before deployment, and verify cargo_score and cargo_tier are selected on the accounts model.

Risk: A broad CRM credential can expose more account data than the skill needs.

Mitigation: Use a credential limited to the account fields required for scoring and CRM write-back where the CRM supports scoped credentials.

Risk: The weekly re-score gate depends on cargo_last_updated_at behaving as intended.

Mitigation: Run cargo-ai cdk plan, test on a small sample account set, and verify the timestamp is written and used correctly before broad deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cargo-ai/skills/account-scoring)
- [Account Scoring Homepage](https://github.com/getcargohq/gtm-skills/tree/main/account-scoring)
- [Cargo GTM Skills Homepage](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript Cargo CDK code, JSON-shaped scoring outputs, configuration notes, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deployed scorer returns score, tier, and rationale; deployment guidance should be reviewed with cargo-ai cdk plan before deploy.]

## Skill Version(s):

0.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
