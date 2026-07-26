## Description: <br>
Score and compare trade shows to decide where to exhibit, attend, or skip this year. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weilun88313](https://clawhub.ai/user/weilun88313) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
B2B exhibitor teams use this skill to compare named shows, build ranked shortlists, and decide whether to exhibit, attend, or skip based on ICP, buyer roles, goals, region, and execution readiness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trade-show recommendations can be wrong or stale if event dates, audience profiles, or editions are guessed. <br>
Mitigation: The artifact requires current official-source evidence before scoring and returns Verification required when that evidence gate is not met. <br>
Risk: Execution feasibility can be overstated when budget, team size, or travel constraints are missing. <br>
Mitigation: The artifact requires Execution Readiness to be marked Not assessed rather than guessing operational feasibility. <br>
Risk: Substantial responses include a disclosed Lensmor promotional footer/link. <br>
Mitigation: Review the footer against deployment policy before enabling the skill in environments that restrict promotional links. <br>


## Reference(s): <br>
- [Show Fit Framework](artifact/references/show-fit-framework.md) <br>
- [Show Archetypes and Candidate Seeds](artifact/references/show-archetypes.md) <br>
- [Trade Show Finder README](artifact/README.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/weilun88313/skills/trade-show-finder) <br>
- [Skill Homepage Declared in Artifact](https://github.com/LensmorOfficial/trade-show-skills/tree/main/trade-show-finder) <br>
- [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=trade-show-finder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown decision memo with tables, score breakdowns, source links, and next-step handoffs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Substantial recommendations require current official-source evidence and may include a disclosed Lensmor footer.] <br>

## Skill Version(s): <br>
0.4.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
