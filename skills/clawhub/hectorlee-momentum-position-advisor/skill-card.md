## Description:

Evaluates A-share stock holdings with volume-price momentum patterns and returns HOLD, WATCH, REDUCE, or SELL technical trading research signals with scoring context.

This skill is for research and development only.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run technical momentum diagnostics on stock positions, portfolio files, or scanned symbols. It produces research-oriented hold, watch, reduce, and sell signals, not automated or authoritative investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill imports and executes code from a mutable sibling volume-price-screener directory.

Mitigation: Review or pin the sibling skill before installation, and run the advisor in an isolated virtual environment with locked dependencies.

Risk: Portfolio and previous-decision state can be written to local JSON files.

Mitigation: Back up portfolio files before use, pass explicit .json paths, and review generated state files before relying on subsequent diagnostics.

Risk: The stock signals may be mistaken for automated or authoritative investment advice.

Mitigation: Treat outputs as technical trading research only and require human review before making trading decisions.

Risk: Running the skill in a credential-rich environment increases exposure if dependencies or sibling code are compromised.

Mitigation: Run it in an environment without unnecessary credentials or secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/hectorlee-momentum-position-advisor)
- [Pattern rules](references/pattern_rules.md)
- [hectorlee-volume-price-screener](https://github.com/xiyanjun/hectorlee-volume-price-screener)
- [hectorlee-daily-precision-picker](https://github.com/xiyanjun/hectorlee-daily-precision-picker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Terminal text and Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces technical trading research signals and may reference local portfolio JSON state; human review is required before acting on outputs.]

## Skill Version(s):

1.4.0 (source: server release metadata; artifact frontmatter lists 1.3.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
