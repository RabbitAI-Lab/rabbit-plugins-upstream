## Description:

会员运营 · 马甲实战版 helps agents answer membership operations data questions with simulated chain-store warehouse schemas, formulas, SQL references, dashboard plans, and data quality guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

External business operators, data analysts, and developers use this skill to design or audit membership analytics, define metrics such as RFM, repurchase, retention, and coupon redemption, and produce SQL or dashboard guidance for customer lifecycle operations. Its examples are simulated and should be validated against local data before production use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may adapt simulated membership, order, staff, CDP, or marketing examples to real customer systems without adequate controls.

Mitigation: Use masked or synthetic examples during adaptation, restrict access to authorized roles, and validate outputs against local schemas, edge cases, and controls before production use.

Risk: Audience segments or outreach recommendations could affect real customers if exported or triggered without review.

Mitigation: Confirm consent and opt-out rules, require human review before exporting segments or triggering outreach, and keep simulated examples separate from verified operating results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/majia-huiyuan)
- [Project homepage](https://github.com/maojiebc/majia-huiyuan)
- [README.en.md](artifact/README.en.md)
- [Formula library index](artifact/公式库/README.md)
- [Agent usage guide](artifact/AGENTS.md)
- [Machine-readable index](artifact/llms.txt)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with SQL and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory text grounded in the bundled skill files; simulated numeric examples must not be treated as real business data.]

## Skill Version(s):

1.4.5 (source: ClawHub release evidence, SKILL.md metadata, README.en.md version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
