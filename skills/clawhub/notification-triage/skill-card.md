## Description: <br>
Classify, score, prioritize, and batch notifications while persisting local rules and state for urgent, batched, and ignored messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to reduce notification noise by classifying incoming messages, batching non-urgent items, tracking seen state, and managing per-source triage rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notification content and metadata are persisted locally in triage state files. <br>
Mitigation: Install only where local persistence is acceptable and periodically review or clear the memory/notification-triage state files. <br>
Risk: A first classification can create a lasting per-source rule, so one misclassification can affect future notification handling. <br>
Mitigation: Use --force for test classifications, review rules with --rules, and remove or clear incorrect rules when found. <br>
Risk: Ignored notifications are dropped from runtime queues and only retained in dropped.json for audit. <br>
Mitigation: Review dropped.json periodically and re-evaluate sources configured with ignore rules. <br>
Risk: Commands such as --rules clear, --seen --all, --send, and --digest mutate or clear local triage state. <br>
Mitigation: Use count-limited sends where possible and run destructive or state-clearing commands deliberately after checking pending state. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/notification-triage) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Node.js command examples and local JSON state descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs notification classifications, batch summaries, status reports, rule listings, and digest text; local state is stored under memory/notification-triage.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release metadata, SKILL.md frontmatter, clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
