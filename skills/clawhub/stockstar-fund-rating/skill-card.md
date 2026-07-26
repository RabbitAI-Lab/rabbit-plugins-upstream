## Description: <br>
Queries public fund rating data from Stockstar for seven rating institutions and helps agents summarize star ratings by fund code or fund name. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stockstar1996](https://clawhub.ai/user/stockstar1996) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up Chinese public fund ratings from Stockstar by six-digit fund code or fund name, then present the available ratings from seven institutions in Chinese. It is useful for fund-rating questions where the user needs current source-backed rating details rather than invented financial data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts fund.stockstar.com and maintains a local cache of public fund-rating data. <br>
Mitigation: Installers should expect purpose-aligned network fetching and local cache writes before deployment. <br>
Risk: Broad finance wording may activate the skill when a user did not intend a fund-rating lookup. <br>
Mitigation: Use clearer fund-rating queries or six-digit fund codes to reduce accidental activation. <br>
Risk: Fund ratings can be unavailable, stale, or absent for a requested fund. <br>
Mitigation: The agent should report not-found or unrated statuses plainly and avoid inventing ratings. <br>


## Reference(s): <br>
- [Stockstar Fund Rating Data Source](https://fund.stockstar.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/stockstar1996/skills/stockstar-fund-rating) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON] <br>
**Output Format:** [Chinese natural-language summaries and Markdown tables derived from JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses fund code or fund name queries and may return disambiguation prompts, not-found messages, or per-institution rating rows.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
