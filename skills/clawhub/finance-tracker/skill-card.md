## Description: <br>
Finance Tracker helps agents log expenses and income, manage recurring subscriptions, track goals and assets, convert currencies, and produce personal finance summaries from a local CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[salen-project](https://clawhub.ai/user/salen-project) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users can use this skill to track personal finance activity from natural-language-style CLI commands, including expenses, recurring items, savings goals, assets, budgets, reports, and exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores sensitive expenses, income, goals, assets, and cached exchange rates in ~/.finance-tracker. <br>
Mitigation: Install and run it only when local storage of personal finance records is acceptable, and avoid sharing exports or logs without reviewing them. <br>
Risk: Commands such as edit, delete, undo, remove, and recurring process can modify or remove finance records. <br>
Mitigation: Review mutating commands before execution, especially when an agent is operating automatically or from a recurring workflow. <br>
Risk: Currency features may contact third-party exchange-rate providers. <br>
Mitigation: Use rates, convert, and foreign-currency expense commands only when external exchange-rate lookups are acceptable. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text and Markdown guidance, with optional CSV and JSON exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores finance records in local files under ~/.finance-tracker and may cache exchange rates locally.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and user-provided target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
